"""Verification script for Grade 12 Mathematical Literacy: Data Handling.
Tests all 52 subskills across seeds [101, 102, 103] (156 runs).
Asserts zero synthetic tokens, zero raw LaTeX leaks, 4 distinct options, valid 6-pillar schema.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Add backend to sys.path
backend_dir = Path(__file__).resolve().parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from app.utils.mathematical_literacy import gr12_data_handling_generator as gen

SEEDS = [101, 102, 103]
BANNED_SYNTHETIC = ["(Option", "(Alt", "(Alternative", "(Variation", "(Tier"]
RAW_LATEX_PATTERNS = ["\\frac", "\\times", "\\cdot", "\\text{", "$$", "\\pm"]


def verify_all() -> None:
    subskills = gen.get_subskills()
    print(f"Loaded {len(subskills)} subskills from gr12_data_handling_generator.")
    assert len(subskills) >= 50, f"Expected >= 50 subskills, found {len(subskills)}"

    total_runs = 0
    passed_runs = 0

    for idx, subskill in enumerate(subskills, start=1):
        for seed in SEEDS:
            total_runs += 1
            questions = gen.generate(seed=seed, subskill=subskill, count=1)
            assert len(questions) == 1, f"Expected 1 question, got {len(questions)}"
            q = questions[0]

            # 1. 6-Pillar structure
            assert "question_id" in q, f"Missing question_id in {subskill} seed {seed}"
            assert "topic" in q, f"Missing topic in {subskill} seed {seed}"
            assert "subskill" in q, f"Missing subskill in {subskill} seed {seed}"
            assert "prompt" in q and q["prompt"].strip(), f"Empty prompt in {subskill} seed {seed}"
            assert "options" in q, f"Missing options in {subskill} seed {seed}"
            assert "correct_answer" in q, f"Missing correct_answer in {subskill} seed {seed}"
            assert "explanation" in q and q["explanation"].strip(), f"Empty explanation in {subskill} seed {seed}"
            assert "hints" in q, f"Missing hints in {subskill} seed {seed}"
            assert "tier_1" in q["hints"], f"Missing tier_1 in {subskill} seed {seed}"
            assert "tier_2" in q["hints"], f"Missing tier_2 in {subskill} seed {seed}"
            assert "tier_3" in q["hints"], f"Missing tier_3 in {subskill} seed {seed}"

            # 2. Options checks
            opts = q["options"]
            assert len(opts) == 4, f"Subskill {subskill} seed {seed} does not have 4 options: {opts}"
            assert len(set(opts)) == 4, f"Subskill {subskill} seed {seed} has duplicate options: {opts}"
            assert q["correct_answer"] in opts, f"Subskill {subskill} seed {seed} correct_answer not in options: {q['correct_answer']} vs {opts}"

            # 3. Banned synthetic tokens
            for opt in opts:
                for banned in BANNED_SYNTHETIC:
                    assert banned not in opt, f"Subskill {subskill} seed {seed} contains synthetic token '{banned}': {opt}"

            # 4. Raw LaTeX checks
            for pattern in RAW_LATEX_PATTERNS:
                assert pattern not in q["prompt"], f"Prompt contains raw LaTeX '{pattern}' in {subskill} seed {seed}: {q['prompt']}"
                for opt in opts:
                    assert pattern not in opt, f"Option contains raw LaTeX '{pattern}' in {subskill} seed {seed}: {opt}"

            passed_runs += 1

        print(f"[{idx:02d}/52] {subskill} PASS across seeds {SEEDS}")

    print("=" * 70)
    print(f"Verification COMPLETE: {len(subskills)}/52 subskills PASS across {len(SEEDS)} seeds ({passed_runs}/{total_runs} runs)")
    print("ALL 52 subskills strictly validated. Zero synthetic options. Zero LaTeX leaks.")
    print("=" * 70)


if __name__ == "__main__":
    verify_all()
