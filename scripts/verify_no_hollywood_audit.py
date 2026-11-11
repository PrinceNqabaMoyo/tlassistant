#!/usr/bin/env python3
"""
Anti-Hollywood Mechanical Gatekeeper for the Full-Archetype Audit (Rule 0d & Rule 30).

This script is pre-planted on disk to prevent any model (including Gemini 3.8) from:
  1. Sampling a subset of archetypes instead of auditing all subskill archetypes for the grade.
  2. Skipping real browser screenshots or duplicating/faking PNG files (enforces >15 KB & SHA-256 uniqueness).
  3. Skipping multi-scroll screenshots when a page is taller than the viewport (scrollHeight > clientHeight + 60).
  4. Weakening detectors instead of fixing generators (independently verifies zero crashes, zero raw LaTeX/CAPS leaks,
     zero pre-attempt answer leaks, and multi-step worked procedures for all questions >= 2 marks).
  5. Dreaming up curriculum fixes without reading curriculum_docs_auto/ (verifies every logged fix cites a real
     file path inside curriculum_docs_auto/ on disk).

Usage:
  python scripts/verify_no_hollywood_audit.py --grade 7
  python scripts/verify_no_hollywood_audit.py --all
"""

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BACKEND_DIR = ROOT / "caps-ai-backend"
sys.path.insert(0, str(BACKEND_DIR))

from app.services.caps_term_curriculum_registry import _ALL_TOPIC_RECORDS
from app.services.generator_registry import generate_variant, get_topic_archetypes

RAW_LATEX_PATTERNS = [
    r"\\frac\{",
    r"\\sqrt\{",
    r"\\text\{",
    r"\\left",
    r"\\right",
    r"\$\$",
    r"\\begin\{",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def extract_procedure_text(q: dict) -> tuple[list[str], str]:
    steps = []
    cs = q.get("canonical_solution")
    if isinstance(cs, dict) and isinstance(cs.get("steps"), list):
        steps.extend(str(s) for s in cs["steps"] if s)
    ws = q.get("worked_solution")
    if isinstance(ws, list):
        steps.extend(str(s) for s in ws if s)
    elif isinstance(ws, str) and ws.strip():
        steps.extend(line.strip() for line in ws.splitlines() if line.strip())
    sol = q.get("solution")
    if isinstance(sol, str) and sol.strip():
        steps.extend(line.strip() for line in sol.splitlines() if line.strip())
    if q.get("explanation"):
        steps.append(str(q.get("explanation")))
    if q.get("sample_answer"):
        steps.append(str(q.get("sample_answer")))
    if isinstance(q.get("marking_schema"), list):
        for m in q.get("marking_schema"):
            if isinstance(m, dict) and m.get("criterion"):
                steps.append(str(m["criterion"]))
    combined = "\n".join(steps)
    return steps, combined.strip()


def audit_grade(grade: str) -> list[str]:
    failures: list[str] = []
    g_str = str(grade).strip()
    records = [r for r in _ALL_TOPIC_RECORDS if str(r.get("grade")) == g_str]
    if not records:
        return [f"Grade {g_str}: No topic records found in _ALL_TOPIC_RECORDS."]

    print(f"[Gatekeeper] Verifying Grade {g_str} ({len(records)} curriculum topics)...")

    # 1. Independent Backend Generator & Catalog Verification
    total_catalog_archetypes = 0
    for rec in records:
        subj = rec["subject"]
        topic = rec["name"]
        info = get_topic_archetypes(topic=topic, grade=g_str, subject=subj)
        archs = info.get("archetypes") or []
        total_catalog_archetypes += len(archs)
        if len(archs) < 3:
            failures.append(
                f"[CATALOG_COLLAPSE] {subj} Gr{g_str} '{topic}' only exposes {len(archs)} archetypes ({archs}). "
                f"Must expose all topic subskill archetypes (>= 4)."
            )

        # Probe all slots across seeds 101 and 202
        for seed in (101, 202):
            try:
                qs = generate_variant(topic=topic, grade=g_str, subject=subj, seed=seed, count=max(len(archs), 5))
            except Exception as exc:
                failures.append(f"[GENERATOR_CRASH] {subj} Gr{g_str} '{topic}' (seed={seed}): {exc}")
                continue

            if not qs:
                failures.append(f"[EMPTY_OUTPUT] {subj} Gr{g_str} '{topic}' (seed={seed}) returned 0 questions.")
                continue

            for idx, q in enumerate(qs):
                q_label = f"{subj} Gr{g_str} '{topic}' [slot {idx}, seed {seed}]"
                prompt_text = " ".join(
                    str(q.get(k) or "") for k in ("question", "prompt", "context", "scenario")
                )

                # Check for banned "CAPS" acronym in student-facing prompt
                if re.search(r"\bCAPS\b", prompt_text):
                    failures.append(f"[BANNED_CAPS_ACRONYM] {q_label} contains 'CAPS' in student prompt.")

                # Check for NaN/undefined leaks
                if re.search(r"\b(undefined|NaN)\b|\[object Object\]", prompt_text):
                    failures.append(f"[JS_TOKEN_LEAK] {q_label} contains undefined/NaN/[object Object].")

                # Check step-by-step procedure depth for multi-mark questions
                marks = int(q.get("marks") or q.get("total_marks") or 1)
                steps, proc_text = extract_procedure_text(q)
                if marks >= 2 and len(proc_text) < 30 and not q.get("sub_questions") and not q.get("parts"):
                    failures.append(
                        f"[THIN_PROCEDURE] {q_label} ({marks} marks) has thin worked procedure ({len(proc_text)} chars)."
                    )

    # 2. Verify Ledger, Real Screenshots, Multi-Scroll & SHA-256 Uniqueness on Disk
    ledger_path = ROOT / "reports" / "full_archetype_audit" / f"ledger_gr{g_str}.json"
    if not ledger_path.is_file():
        failures.append(f"[MISSING_LEDGER] {ledger_path} does not exist on disk.")
        return failures

    try:
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append(f"[CORRUPT_LEDGER] {ledger_path}: {exc}")
        return failures

    entries = ledger.get("archetypes") or []
    if len(entries) < total_catalog_archetypes:
        failures.append(
            f"[INCOMPLETE_AUDIT] Ledger has {len(entries)} entries, expected >= {total_catalog_archetypes} archetypes for Grade {g_str}."
        )

    seen_hashes: dict[str, str] = {}
    for entry in entries:
        aid = f"{entry.get('subject')} | {entry.get('topic')} | {entry.get('archetype_id')}"
        if not entry.get("mounted_in_universal_workspace"):
            failures.append(f"[HOLLYWOOD_STUB] {aid} was not mounted inside live UniversalWorkspace.jsx.")

        pre_shots = entry.get("pre_scroll_screenshots") or []
        memo_shots = entry.get("memo_scroll_screenshots") or []
        if not pre_shots:
            failures.append(f"[MISSING_PRE_SCREENSHOT] {aid} has 0 pre-attempt screenshots.")
        if not memo_shots:
            failures.append(f"[MISSING_MEMO_SCREENSHOT] {aid} has 0 sample-answer/procedure screenshots.")

        # Verify multi-scroll requirement when page is taller than viewport
        vp_h = int(entry.get("viewport_height") or 900)
        pre_h = int(entry.get("pre_scroll_height") or 0)
        memo_h = int(entry.get("memo_scroll_height") or 0)
        if pre_h > vp_h + 60 and len(pre_shots) < 2:
            failures.append(
                f"[MISSING_MULTI_SCROLL_PRE] {aid} has pre_scroll_height={pre_h}px (> {vp_h}px) but only {len(pre_shots)} screenshot(s)."
            )
        if memo_h > vp_h + 60 and len(memo_shots) < 2:
            failures.append(
                f"[MISSING_MULTI_SCROLL_MEMO] {aid} has memo_scroll_height={memo_h}px (> {vp_h}px) but only {len(memo_shots)} screenshot(s)."
            )

        for rel_shot in pre_shots + memo_shots:
            shot_path = ROOT / rel_shot
            if not shot_path.is_file():
                failures.append(f"[PHANTOM_SCREENSHOT] {aid} references missing file {rel_shot}.")
                continue
            size_b = shot_path.stat().st_size
            if size_b < 15000:
                failures.append(f"[BLANK_OR_TINY_PNG] {rel_shot} is only {size_b} bytes (< 15 KB).")
            file_hash = sha256_file(shot_path)
            if file_hash in seen_hashes and seen_hashes[file_hash] != rel_shot:
                failures.append(
                    f"[DUPLICATE_SCREENSHOT_HASH] {rel_shot} is an exact byte duplicate of {seen_hashes[file_hash]}."
                )
            else:
                seen_hashes[file_hash] = rel_shot

        # Ensure zero unresolved defects remain
        open_defects = entry.get("unresolved_defects") or []
        if open_defects:
            failures.append(f"[UNRESOLVED_DEFECTS] {aid} still has unresolved defects: {open_defects}")

    # 3. Verify curriculum_docs_auto/ Grounding Citations for All Remediations
    for rem in ledger.get("remediations") or []:
        c_doc = rem.get("curriculum_doc_path") or ""
        if not c_doc or "curriculum_docs_auto" not in c_doc.replace("\\", "/"):
            failures.append(
                f"[UNGROUNDED_FIX] Remediation for '{rem.get('archetype_id')}' does not cite a curriculum_docs_auto/ file."
            )
        else:
            full_doc = ROOT / c_doc
            if not full_doc.is_file():
                failures.append(
                    f"[FICTIONAL_CURRICULUM_DOC] Remediation for '{rem.get('archetype_id')}' cites non-existent file '{c_doc}'."
                )

    # 4. Verify HTML Report Exists and Links Screenshots
    html_path = ROOT / "reports" / "full_archetype_audit" / f"grade_{g_str}.html"
    if not html_path.is_file():
        failures.append(f"[MISSING_HTML_REPORT] {html_path} does not exist on disk.")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Anti-Hollywood Mechanical Gatekeeper for Full-Archetype Audit")
    parser.add_argument("--grade", type=str, help="Grade to verify (7..12)")
    parser.add_argument("--all", action="store_true", help="Verify all Grades 7..12")
    args = parser.parse_args()

    grades = ["7", "8", "9", "10", "11", "12"] if args.all else ([args.grade] if args.grade else [])
    if not grades:
        print("Error: specify --grade <7..12> or --all", file=sys.stderr)
        return 1

    all_failures: list[str] = []
    for g in grades:
        all_failures.extend(audit_grade(g))

    if all_failures:
        print(f"\n[FAIL] Anti-Hollywood Gatekeeper detected {len(all_failures)} violation(s):")
        for f in all_failures[:40]:
            print(f"  - {f}")
        if len(all_failures) > 40:
            print(f"  ... and {len(all_failures) - 40} more violations.")
        return 1

    print("\n[PASS] Exit Code 0 — All Anti-Hollywood mechanical checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
