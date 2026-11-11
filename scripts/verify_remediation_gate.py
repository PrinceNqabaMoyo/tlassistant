#!/usr/bin/env python3
"""Fundile Mechanical Remediation Gatekeeper (scripts/verify_remediation_gate.py).

Designed to eliminate partial ("1-of-N") remediation, alias hijacking, missing
memorandum tables, un-unwrapped bundle stubs, raw markdown header leaks, and
cross-grade syllabus bleed.

Usage:
  python scripts/verify_remediation_gate.py --grade 10,11,12 --subject "Accounting"
  python scripts/verify_remediation_gate.py --grade 7,8,9 --subject "Economic and Management Sciences,Mathematics,Natural Sciences"
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
BACKEND_DIR = ROOT / "caps-ai-backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.services.generator_registry import (  # noqa: E402
    ALL_GENERATORS,
    generate_variant,
    get_topic_archetypes,
    resolve_generator_key,
)

REGISTRY_JSON = BACKEND_DIR / "app" / "services" / "caps_term_registry_data.json"

BANNED_PROSE_TOKENS = ("pontsho", "lonely traders")
RAW_HEADER_RE = re.compile(r"#{3,6}\s*(?:REQUIRED|INFORMATION)\b", re.IGNORECASE)
DEF_PLACEHOLDER_RE = re.compile(r"\bDef\s+[0-9]+\b")


def _norm_subj(s: str) -> str:
    s_low = s.strip().lower()
    if s_low in ("ems", "economic and management sciences"):
        return "economic and management sciences"
    if s_low in ("math", "maths", "mathematics"):
        return "mathematics"
    if s_low in ("ns", "natural sciences", "natural science"):
        return "natural sciences"
    if s_low in ("acc", "accounting"):
        return "accounting"
    return s_low


def run_gate(grades: List[str], subjects: List[str], seeds: int = 12, min_subskills: int = 4) -> int:
    records = json.loads(REGISTRY_JSON.read_text(encoding="utf-8"))
    norm_grades = {str(g).strip() for g in grades if str(g).strip()}
    norm_subjects = {_norm_subj(s) for s in subjects if s.strip()}

    filtered: List[Dict[str, Any]] = []
    for rec in records:
        g = str(rec.get("grade", "")).strip()
        s = _norm_subj(str(rec.get("subject", "")))
        if norm_grades and g not in norm_grades:
            continue
        if norm_subjects and s not in norm_subjects:
            continue
        filtered.append(rec)

    if not filtered:
        print(f"[FAIL] No curriculum topics matched grades={grades} subjects={subjects}")
        return 1

    print("=" * 78)
    print(f"FUNDILE REMEDIATION GATEKEEPER — Auditing {len(filtered)} Topics ({seeds} seeds/topic)")
    print("=" * 78)

    failures: List[str] = []
    key_usage: Dict[Tuple[str, str], List[str]] = defaultdict(list)

    for rec in sorted(filtered, key=lambda r: (int(r["grade"]), r["subject"], int(r.get("term", 1)), r["name"])):
        grade = str(rec["grade"])
        subject = str(rec["subject"])
        topic = str(rec["name"])
        manifest_key = str(rec.get("generator_key", ""))
        resolved_key = resolve_generator_key(topic, grade=grade, subject=subject)

        # Gate 1: Resolution & 1:1 Unbundling Check
        if not resolved_key or resolved_key not in ALL_GENERATORS:
            failures.append(f"[G{grade} {subject}] '{topic}': Unresolved generator key '{resolved_key}' (manifest='{manifest_key}')")
            continue
        if manifest_key != resolved_key:
            failures.append(f"[G{grade} {subject}] '{topic}': Alias hijack detected! Manifest='{manifest_key}' != Resolved='{resolved_key}'")

        key_usage[( _norm_subj(subject), resolved_key )].append(f"Gr{grade}:{topic}")

        subskills_seen: Set[str] = set()
        tabular_count = 0
        memo_table_count = 0
        topic_errors: List[str] = []

        # Probe via get_topic_archetypes + multi-seed single calls
        try:
            arch_info = get_topic_archetypes(topic=topic, grade=grade, subject=subject)
            for a in arch_info.get("archetypes", []):
                if a and not str(a).endswith(("_subskill_1", "_subskill_2", "_subskill_3", "_subskill_4", "_subskill_5")):
                    subskills_seen.add(str(a))
        except Exception as exc:
            topic_errors.append(f"get_topic_archetypes error: {exc}")

        for s_idx in range(1, seeds + 1):
            try:
                qs = generate_variant(topic=topic, grade=grade, subject=subject, seed=s_idx * 13, count=1)
                if not qs:
                    topic_errors.append(f"seed {s_idx}: returned empty list")
                    continue
                q = qs[0]
                sub = str(q.get("subskill") or q.get("archetype") or "").strip()
                if sub and sub != "unknown":
                    subskills_seen.add(sub)

                qtype = str(q.get("question_type") or "").lower()
                if qtype == "bundle":
                    topic_errors.append(f"seed {s_idx}: un-unwrapped 'bundle' question_type")

                prompt = str(q.get("prompt") or q.get("question") or "")
                memo = str(q.get("worked_solution") or q.get("canonical_solution") or "")
                combined_low = (prompt + "\n" + memo).lower()

                for banned in BANNED_PROSE_TOKENS:
                    if banned in combined_low:
                        topic_errors.append(f"seed {s_idx}: contains banned token '{banned}'")

                if RAW_HEADER_RE.search(prompt):
                    topic_errors.append(f"seed {s_idx}: raw markdown header ('#### REQUIRED/INFORMATION') in prompt")

                if DEF_PLACEHOLDER_RE.search(prompt + "\n" + memo):
                    topic_errors.append(f"seed {s_idx}: raw 'Def 0/1/2' placeholder leaked")

                is_tabular = bool(
                    q.get("modality") == "ledger"
                    or q.get("rows")
                    or q.get("journal")
                    or q.get("table_schema")
                    or q.get("table")
                )
                if is_tabular:
                    tabular_count += 1
                    if "|" in memo and memo.count("\n|") >= 2:
                        memo_table_count += 1
                    else:
                        topic_errors.append(f"seed {s_idx} ({sub}): tabular question missing completed Markdown table in Memorandum")
            except Exception as exc:
                topic_errors.append(f"seed {s_idx} exception: {exc}")

        if len(subskills_seen) < min_subskills:
            failures.append(
                f"[G{grade} {subject}] '{topic}' ({resolved_key}): Only {len(subskills_seen)} subskills emitted (< {min_subskills}): {sorted(subskills_seen)}"
            )
        if topic_errors:
            failures.append(f"[G{grade} {subject}] '{topic}' ({resolved_key}): {len(topic_errors)} error(s): {topic_errors[:3]}")
        else:
            print(
                f"  [PASS] Gr{grade:<2} | {subject:<32} | {topic:<48} | subs={len(subskills_seen):<2} | tbl_memo={memo_table_count}/{tabular_count}"
            )

    # Check cross-topic / cross-grade sharing within same subject
    for (subj_norm, gkey), topic_list in key_usage.items():
        if len(topic_list) > 1:
            failures.append(f"[SHARED GENERATOR VIOLATION] '{gkey}' is shared across {len(topic_list)} topics: {topic_list}")

    print("=" * 78)
    if failures:
        print(f"[FAIL] REMEDIATION GATE FAILED WITH {len(failures)} VIOLATION(S):")
        for f in failures:
            print(f"  - {f}")
        print("=" * 78)
        return 1

    print(f"[PASS] ALL {len(filtered)} TOPICS PASSED ALL REMEDIATION GATES (EXIT CODE 0).")
    print("=" * 78)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Fundile Mechanical Remediation Gatekeeper")
    parser.add_argument("--grade", type=str, required=True, help="Comma-separated grades, e.g. 10,11,12 or 7,8,9")
    parser.add_argument("--subject", type=str, required=True, help="Comma-separated subjects, e.g. Accounting")
    parser.add_argument("--seeds", type=int, default=12, help="Seeds per topic to probe")
    parser.add_argument("--min-subskills", type=int, default=4, help="Minimum distinct subskills required per topic")
    args = parser.parse_args()

    grades = [g.strip() for g in args.grade.split(",") if g.strip()]
    subjects = [s.strip() for s in args.subject.split(",") if s.strip()]
    return run_gate(grades=grades, subjects=subjects, seeds=args.seeds, min_subskills=args.min_subskills)


if __name__ == "__main__":
    sys.exit(main())
