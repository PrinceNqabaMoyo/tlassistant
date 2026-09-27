"""Curriculum Service — Pure Python, zero-RAG, zero-ChromaDB curriculum browser.

Grounded directly in `caps-wiki/` Markdown files as mandated by Rule 11:
"Deterministic Context, Not RAG. The agent is grounded by reading the relevant
caps-wiki/ Markdown file directly."
"""
from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional


class CurriculumService:
    def __init__(self, wiki_dir: Optional[str] = None):
        if wiki_dir:
            self.wiki_path = Path(wiki_dir)
        else:
            base_backend = Path(__file__).resolve().parent.parent.parent
            self.wiki_path = base_backend / "caps-wiki"

    def get_curriculum_data(self) -> Dict[str, Any]:
        """Scans `caps-wiki/` and returns structured curriculum data by subject and grade."""
        if not self.wiki_path.exists():
            return self._get_fallback_curriculum_data()

        curriculum_data: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}

        for subject_dir in self.wiki_path.iterdir():
            if not subject_dir.is_dir() or subject_dir.name.startswith("."):
                continue
            subject_key = subject_dir.name.lower().replace("-", "_")
            curriculum_data[subject_key] = {}

            for grade_dir in subject_dir.iterdir():
                if not grade_dir.is_dir() or grade_dir.name.startswith("."):
                    continue
                grade_key = grade_dir.name.lower().replace("-", "_")
                topics_list: List[Dict[str, Any]] = []

                for topic_file in grade_dir.glob("*.md"):
                    topic_name = topic_file.stem.replace("_", " ").title()
                    # Read brief summary / first paragraph
                    desc = ""
                    try:
                        content = topic_file.read_text(encoding="utf-8")
                        lines = [line.strip() for line in content.splitlines() if line.strip() and not line.startswith("#")]
                        if lines:
                            desc = lines[0][:160] + "..." if len(lines[0]) > 160 else lines[0]
                    except Exception:
                        desc = f"Curriculum topic for {topic_name}"

                    topics_list.append({
                        "name": topic_name,
                        "file": topic_file.name,
                        "description": desc,
                        "estimated_hours": 3,
                    })

                if topics_list:
                    curriculum_data[subject_key][grade_key] = topics_list

        return curriculum_data if curriculum_data else self._get_fallback_curriculum_data()

    def get_topics_by_subject_grade(self, subject: str, grade: str) -> List[Dict[str, Any]]:
        """Get topics for a specific subject and grade directly from caps-wiki."""
        subj_clean = subject.lower().replace("_", "-")
        grade_clean = grade.lower().replace("_", "-")
        target_dir = self.wiki_path / subj_clean / grade_clean

        if not target_dir.exists():
            # Try alternate naming
            subj_alt = subject.lower().replace("-", "_")
            grade_alt = grade.lower().replace("-", "_")
            target_dir = self.wiki_path / subj_alt / grade_alt

        if not target_dir.exists():
            fallback = self._get_fallback_curriculum_data()
            return fallback.get(subject.lower().replace("-", "_"), {}).get(grade.lower().replace("-", "_"), [])

        topics = []
        for f in target_dir.glob("*.md"):
            topic_name = f.stem.replace("_", " ").title()
            desc = ""
            try:
                content = f.read_text(encoding="utf-8")
                lines = [l.strip() for l in content.splitlines() if l.strip() and not l.startswith("#")]
                if lines:
                    desc = lines[0][:160]
            except Exception:
                desc = topic_name

            topics.append({
                "name": topic_name,
                "file": f.name,
                "description": desc,
                "path": str(f),
            })
        return topics

    def search_curriculum(self, query: str, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Searches markdown files in caps-wiki using fast pure-Python keyword scanning."""
        if not query or not self.wiki_path.exists():
            return []

        query_terms = [q.lower() for q in query.split() if len(q) > 2]
        if not query_terms:
            return []

        results: List[Dict[str, Any]] = []

        for md_path in self.wiki_path.glob("**/*.md"):
            try:
                text = md_path.read_text(encoding="utf-8")
                text_lower = text.lower()
                matches = sum(text_lower.count(term) for term in query_terms)
                if matches > 0:
                    rel_parts = md_path.relative_to(self.wiki_path).parts
                    subj = rel_parts[0] if len(rel_parts) > 0 else ""
                    grd = rel_parts[1] if len(rel_parts) > 1 else ""

                    # Check filters if present
                    if filters:
                        if filters.get("subject") and filters["subject"].lower() not in subj.lower():
                            continue
                        if filters.get("grade") and filters["grade"].lower() not in grd.lower():
                            continue

                    # Extract matching excerpt
                    first_pos = min(text_lower.find(t) for t in query_terms if t in text_lower)
                    start = max(0, first_pos - 80)
                    end = min(len(text), first_pos + 160)
                    snippet = "..." + text[start:end].replace("\n", " ").strip() + "..."

                    results.append({
                        "subject": subj,
                        "grade": grd,
                        "topic": md_path.stem.replace("_", " ").title(),
                        "content": snippet,
                        "relevance_score": matches,
                        "file_path": str(md_path),
                    })
            except Exception:
                continue

        # Sort by relevance
        results.sort(key=lambda x: x["relevance_score"], reverse=True)
        return results[:20]

    def _get_fallback_curriculum_data(self) -> Dict[str, Any]:
        """Fallback curriculum hierarchy when files are unavailable."""
        return {
            "mathematics": {
                "grade_10": [
                    {"name": "Algebraic Expressions", "description": "Expansion, factorisation and fractions", "estimated_hours": 3},
                    {"name": "Equations and Inequalities", "description": "Linear and quadratic equations", "estimated_hours": 4},
                    {"name": "Euclidean Geometry", "description": "Triangles and quadrilaterals", "estimated_hours": 4},
                ],
                "grade_11": [
                    {"name": "Circle Geometry", "description": "Theorems on angles, cyclic quads and tangents", "estimated_hours": 5},
                ],
            },
            "business_studies": {
                "grade_10": [
                    {"name": "Micro Environment", "description": "Internal business components", "estimated_hours": 3},
                    {"name": "Market Environment", "description": "Consumers, suppliers, competitors", "estimated_hours": 3},
                ]
            },
        }
