"""Curriculum document parser for Business Studies section-based progression.

Reads `.md` topic files from `curriculum_docs/` and derives scaffold steps
with recommended question formats per section.
"""
from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Map topic keys → relative paths under curriculum_docs/
# These are the actual curriculum .md files that drive progression.
TOPIC_MD_MAP: Dict[str, str] = {
    # Term 1
    "grade10_bs_micro_environment": "BusinessStudies_Gr10/Term-1/1 Components of the  Micro environment.md",
    "grade10_bs_business_functions": "BusinessStudies_Gr10/Term-1/2 Business functions and the activities of the business.md",
    "grade10_bs_market_environment": "BusinessStudies_Gr10/Term-1/3 The market environment.md",
    "grade10_bs_macro_environment": "BusinessStudies_Gr10/Term-1/4 The macro environment.md",
    "grade10_bs_interrelationship": "BusinessStudies_Gr10/Term-2/5 The interrelationship of the micro, market an...",
    "grade10_bs_business_sectors": "BusinessStudies_Gr10/Term-2/6 Business sectors.md",
    # Term 2
    "grade10_bs_socio_economic_issues": "BusinessStudies_Gr10/Term-2/7 Contemporary socio-economic issues.md",
    "grade10_bs_social_responsibility": "BusinessStudies_Gr10/Term-2/8 Social responsibility.md",
    "grade10_bs_entrepreneurial_qualities": "BusinessStudies_Gr10/Term-2/9 Entrepreneurial qualities.md",
    "grade10_bs_forms_of_ownership": "BusinessStudies_Gr10/Term-2/10 Forms of ownership.md",
    "grade10_bs_concept_of_quality": "BusinessStudies_Gr10/Term-2/11 The concept of quality.md",
    # Term 3 topics without known .md files yet — will return empty sections
}


def _curriculum_docs_dir() -> Path:
    """Return the absolute path to curriculum_docs."""
    # From caps-ai-backend/app/utils/grade10_business_studies/
    # go up to caps-ai-backend, then into curriculum_docs
    here = Path(__file__).resolve().parent
    backend_root = here.parent.parent.parent  # app/utils/grade10_business_studies → app/utils → app → caps-ai-backend
    return backend_root / "curriculum_docs"


def _find_md_file(rel_path: str) -> Optional[Path]:
    """Find the actual .md file, accounting for Windows path truncation."""
    base = _curriculum_docs_dir()
    # Try exact path first
    exact = base / rel_path
    if exact.exists():
        return exact

    # If the filename is truncated (ends with ...), scan the directory
    if rel_path.endswith("..."):
        parent_dir = base / Path(rel_path).parent
        if parent_dir.exists():
            stem = Path(rel_path).name.rstrip(".")
            for f in parent_dir.iterdir():
                if f.is_file() and f.suffix == ".md" and f.stem.startswith(stem):
                    return f
    return None


def _slugify(text: str) -> str:
    """Convert a heading to a URL-safe slug."""
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s-]+", "_", s)
    return s[:64]


def _extract_headings(text: str) -> List[Tuple[int, str]]:
    """Extract all ### and #### headings from markdown text."""
    headings = []
    for match in re.finditer(r"^(#{3,4})\s+(.+)$", text, re.MULTILINE):
        level = len(match.group(1))
        title = match.group(2).strip()
        headings.append((level, title))
    return headings


def _infer_formats(title: str, content: str) -> List[str]:
    """Infer recommended question formats from section heading + content."""
    t = title.lower()
    c = content.lower()

    # Heavyweight decision tree
    if any(word in t for word in ["differences", "compare", "contrast", "versus", "vs"]):
        return ["matching_columns", "word_bank"]
    if any(word in t for word in ["definition", "meaning", "key concepts", "key terms", "glossary"]):
        return ["mcq", "word_bank", "crossword"]
    if any(word in t for word in ["list", "name", "identify", "state", "outline"]):
        return ["mcq", "word_bank"]
    if any(word in t for word in ["discuss", "evaluate", "analyse", "impact", "importance", "advantages", "disadvantages"]):
        return ["typed", "essay"]
    if any(word in t for word in ["explain", "describe", "purpose", "role", "function"]):
        return ["mcq", "typed", "word_bank"]
    if any(word in t for word in ["activity", "exercise", "case study", "scenario"]):
        return ["mcq", "typed", "matching_columns"]
    if any(word in t for word in ["process", "steps", "procedure", "levels"]):
        return ["matching_columns", "crossword", "word_bank"]

    # Content-based heuristics
    if "csv" in c or "table" in c:
        return ["matching_columns", "word_bank"]
    if c.count("•") > 5 or c.count("-") > 10:
        return ["mcq", "word_bank", "matching_columns"]
    if "diagram" in c or "figure" in c:
        return ["mcq", "word_bank"]

    return ["mcq", "typed"]


def parse_md_sections(md_path: str | Path) -> List[Dict[str, Any]]:
    """Parse a curriculum .md file into scaffold sections.

    Returns a list of dicts:
        [
            {
                "key": "understanding_business_functions",
                "title": "Understanding business functions",
                "heading_level": 3,
                "formats": ["mcq", "word_bank"],
            },
            ...
        ]
    """
    path = Path(md_path)
    if not path.exists():
        return []

    text = path.read_text(encoding="utf-8")
    headings = _extract_headings(text)

    if not headings:
        return []

    sections = []
    for i, (level, title) in enumerate(headings):
        # Extract content between this heading and the next heading
        start_match = re.search(re.escape(title), text)
        if not start_match:
            continue
        start_pos = start_match.end()

        # Find the next heading at same or higher level
        next_pos = len(text)
        for j in range(i + 1, len(headings)):
            next_level, next_title = headings[j]
            if next_level <= level:
                m = re.search(re.escape(next_title), text[start_pos:])
                if m:
                    next_pos = start_pos + m.start()
                break

        content = text[start_pos:next_pos]

        slug = _slugify(title)
        sections.append({
            "key": slug,
            "title": title,
            "heading_level": level,
            "formats": _infer_formats(title, content),
        })

    return sections


def get_topic_sections(topic: str) -> List[Dict[str, Any]]:
    """Get scaffold sections for a given topic key."""
    rel_path = TOPIC_MD_MAP.get(topic)
    if not rel_path:
        return []

    md_path = _find_md_file(rel_path)
    if not md_path:
        return []

    return parse_md_sections(md_path)


def get_section_for_topic(topic: str, section_key: str) -> Optional[Dict[str, Any]]:
    """Get a specific section by key for a topic."""
    sections = get_topic_sections(topic)
    for sec in sections:
        if sec["key"] == section_key:
            return sec
    return None
