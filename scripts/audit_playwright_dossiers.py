#!/usr/bin/env python3
"""
Deep Analyzer & Issue Scanner for all generated BKT dossiers in playwright-test/
Reads every single Markdown file and inspects generated questions,
student inputs, expected answers, worked solutions, and semantic curriculum relevance.
"""

import os
import sys
import re
import json
import glob
from collections import defaultdict
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PLAYWRIGHT_DIR = ROOT_DIR / "playwright-test"
VOCAB_PATH = ROOT_DIR / "caps-ai-backend" / "app" / "services" / "curriculum_topic_vocabulary.json"

try:
    from audit_semantic_relevance import verify_text_relevance, SUBJECT_EXCLUSIVE_MARKERS
except ImportError:
    sys.path.insert(0, str(ROOT_DIR / "scripts"))
    from audit_semantic_relevance import verify_text_relevance, SUBJECT_EXCLUSIVE_MARKERS


def load_vocab_manifest():
    if not VOCAB_PATH.exists():
        print(f"Warning: {VOCAB_PATH} does not exist. Run scripts/audit_semantic_relevance.py first.")
        return {}
    with open(VOCAB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def analyze_dossiers():
    files = glob.glob(str(PLAYWRIGHT_DIR / "Gr*" / "*" / "*.md"))
    print(f"Total dossier files found: {len(files)}")
    
    vocab_manifest = load_vocab_manifest()
    
    stats = {
        "total_files": len(files),
        "total_questions_parsed": 0,
        "files_with_short_worked_solutions": [],
        "files_with_truncated_solutions": [],
        "files_with_empty_expected_answers": [],
        "files_with_mcq_missing_options_rendered": [],
        "files_with_low_entropy": [],
        "files_with_raw_json_in_answer": [],
        "files_with_double_braces_in_latex": [],
        "files_with_cross_subject_leaks": [],
        "files_with_zero_topic_keywords": [],
        "subject_breakdown": defaultdict(int),
        "topics_analyzed": set(),
    }

    missing_mcq_options_count = 0
    truncated_solution_count = 0
    empty_expected_count = 0
    short_solutions_count = 0
    double_braces_count = 0
    cross_subject_leak_count = 0
    zero_keyword_count = 0

    for file_path in files:
        if file_path.endswith("PIPELINE_SUMMARY.md"):
            continue

        rel_path = os.path.relpath(file_path, str(PLAYWRIGHT_DIR))
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Split into steps
        steps = re.split(r"### Step \d+:", content)
        header = steps[0]
        question_steps = steps[1:]
        stats["total_questions_parsed"] += len(question_steps)

        # Parse metadata from header table
        topic_match = re.search(r"\|\s*\*\*Topic\*\*\s*\|\s*(.+?)\s*\|", header)
        subject_match = re.search(r"\|\s*\*\*Subject\*\*\s*\|\s*(.+?)\s*\|", header)
        grade_match = re.search(r"\|\s*\*\*Grade\*\*\s*\|\s*(.+?)\s*\|", header)
        genkey_match = re.search(r"\|\s*\*\*Resolved Generator Key\*\*\s*\|\s*`?([^\`\s\|]+)`?\s*\|", header)

        extracted_topic = topic_match.group(1).strip() if topic_match else Path(file_path).stem
        extracted_subject = subject_match.group(1).strip() if subject_match else ""
        extracted_grade_raw = grade_match.group(1).strip() if grade_match else ""
        extracted_grade = re.sub(r"[^\d]", "", extracted_grade_raw) or "10"
        extracted_genkey = genkey_match.group(1).strip() if genkey_match else ""

        stats["subject_breakdown"][f"Gr{extracted_grade} {extracted_subject}"] += 1
        stats["topics_analyzed"].add(f"Gr{extracted_grade}/{extracted_subject}/{extracted_topic}")

        prompts_in_file = []
        file_has_truncated_sol = False
        file_has_empty_expected = False
        file_has_mcq_missing_options = False
        file_has_double_braces = False
        file_cross_subject_leaks = []
        file_questions_with_zero_keywords = 0

        for q_block in question_steps:
            # Check prompt
            prompt_match = re.search(r"\*\*Question Prompt:\*\*\s*\n>\s*(.+?)(?=\n-|\n\*\*Question Sub-Parts|\n\n)", q_block, re.DOTALL)
            prompt_text = prompt_match.group(1).strip() if prompt_match else ""
            if prompt_text:
                prompts_in_file.append(prompt_text)

            # Check MCQ options
            header_line = q_block.split("\n")[0] if q_block else ""
            if "_mcq_" in header_line:
                if "Multiple Choice Options:" not in q_block and "Options:" not in q_block and "**[A]**" not in q_block:
                    file_has_mcq_missing_options = True
                    missing_mcq_options_count += 1

            # Check expected answer
            expected_match = re.search(r"\*\*Expected / Memo Answer:\*\*\s*(.+?)\n", q_block)
            expected_text = expected_match.group(1).strip() if expected_match else ""
            if not expected_text or expected_text in ("`None`", "`null`", "`\"\"`", "``"):
                file_has_empty_expected = True
                empty_expected_count += 1

            # Check worked solution
            sol_match = re.search(r"\*\*Official Worked Solution:\*\*\s*(.+?)\n", q_block)
            sol_text = sol_match.group(1).strip() if sol_match else ""
            if len(sol_text) < 15:
                short_solutions_count += 1
            if sol_text.endswith("...") or "... (truncated)" in sol_text:
                file_has_truncated_sol = True
                truncated_solution_count += 1

            # Check double braces in LaTeX e.g. {{,}}
            if "{{,}}" in q_block:
                file_has_double_braces = True
                double_braces_count += 1

            # Semantic relevance check (using prompt + answer + solution)
            if vocab_manifest and prompt_text:
                full_q_text = f"{prompt_text} {expected_text} {sol_text}"
                rel_check = verify_text_relevance(
                    full_q_text,
                    extracted_subject,
                    extracted_grade,
                    extracted_topic,
                    vocab_manifest
                )
                if rel_check["cross_subject_leaks"]:
                    file_cross_subject_leaks.append(rel_check["cross_subject_leaks"])
                    cross_subject_leak_count += 1
                if rel_check["matched_keywords_count"] == 0:
                    file_questions_with_zero_keywords += 1
                    zero_keyword_count += 1

        # Check prompt entropy in this file (unique prompts / total prompts)
        if len(prompts_in_file) >= 50:
            practice_prompts = prompts_in_file[3:53]
            unique_practice = set(practice_prompts)
            entropy = len(unique_practice) / len(practice_prompts) if practice_prompts else 1.0
            if entropy < 0.25:
                stats["files_with_low_entropy"].append({
                    "file": rel_path,
                    "unique": len(unique_practice),
                    "total": len(practice_prompts),
                    "entropy": round(entropy, 2),
                    "sample": list(unique_practice)[:2]
                })

        if file_has_truncated_sol:
            stats["files_with_truncated_solutions"].append(rel_path)
        if file_has_empty_expected:
            stats["files_with_empty_expected_answers"].append(rel_path)
        if file_has_mcq_missing_options:
            stats["files_with_mcq_missing_options_rendered"].append(rel_path)
        if file_has_double_braces:
            stats["files_with_double_braces_in_latex"].append(rel_path)
        if file_cross_subject_leaks:
            stats["files_with_cross_subject_leaks"].append({
                "file": rel_path,
                "topic": extracted_topic,
                "subject": extracted_subject,
                "leaks": file_cross_subject_leaks[:3]
            })
        if file_questions_with_zero_keywords > (len(question_steps) * 0.7):
            stats["files_with_zero_topic_keywords"].append({
                "file": rel_path,
                "topic": extracted_topic,
                "unmatched_ratio": round(file_questions_with_zero_keywords / max(1, len(question_steps)), 2)
            })

    print("\n" + "="*80)
    print("PLAYWRIGHT TEST DOSSIER DEEP AUDIT RESULTS")
    print("="*80)
    print(f"Total dossier files analyzed: {stats['total_files']}")
    print(f"Total questions analyzed: {stats['total_questions_parsed']}")
    print(f"Empty expected answers: {empty_expected_count} instances in {len(stats['files_with_empty_expected_answers'])} files")
    print(f"MCQ questions missing options in Markdown view: {missing_mcq_options_count} instances in {len(stats['files_with_mcq_missing_options_rendered'])} files")
    print(f"Truncated worked solutions (...): {truncated_solution_count} instances in {len(stats['files_with_truncated_solutions'])} files")
    print(f"Very short worked solutions (<15 chars): {short_solutions_count} instances")
    print(f"Double braces in LaTeX ({{{{,}}}}): {double_braces_count} instances in {len(stats['files_with_double_braces_in_latex'])} files")
    print(f"Files with low question entropy (<25% unique in 50 practice Qs): {len(stats['files_with_low_entropy'])} files")
    print(f"Cross-subject marker violations: {cross_subject_leak_count} instances in {len(stats['files_with_cross_subject_leaks'])} files")
    print(f"Files with >70% vocabulary irrelevance: {len(stats['files_with_zero_topic_keywords'])} files")

    if stats["files_with_cross_subject_leaks"]:
        print(f"\n--- [CRITICAL DEFECT] CROSS-SUBJECT LEAKS DETECTED ({len(stats['files_with_cross_subject_leaks'])} files) ---")
        for item in stats["files_with_cross_subject_leaks"][:10]:
            print(f"  • {item['file']} ({item['subject']} - {item['topic']}): {item['leaks']}")

    if stats["files_with_zero_topic_keywords"]:
        print(f"\n--- [WARNING] TOPIC VOCABULARY UNMATCHED ({len(stats['files_with_zero_topic_keywords'])} files) ---")
        for item in stats["files_with_zero_topic_keywords"][:5]:
            print(f"  • {item['file']} ({item['topic']}): {item['unmatched_ratio']*100}% unmatched")

    return stats


if __name__ == "__main__":
    results = analyze_dossiers()
    # If there are any critical defects (empty answers, truncated solutions, or cross-subject leaks)
    has_critical_failure = (
        len(results["files_with_empty_expected_answers"]) > 0 or
        len(results["files_with_truncated_solutions"]) > 0 or
        len(results["files_with_cross_subject_leaks"]) > 0
    )
    if has_critical_failure:
        print("\nAudit check failed: Critical defects present in dossiers.")
        sys.exit(1)
    else:
        print("\nAudit check PASSED: All dossiers comply with curriculum and format standards.")
        sys.exit(0)
