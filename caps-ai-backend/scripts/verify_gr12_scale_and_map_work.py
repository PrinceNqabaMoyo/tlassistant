import sys
import os

# Ensure backend root in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.utils.mathematical_literacy.gr12_scale_and_map_work_generator import (
    generate,
    get_subskills,
)

def main():
    subskills = get_subskills()
    print(f"Loaded {len(subskills)} subskills for Grade 12 Scale and Map Work.")
    assert len(subskills) >= 50, f"Expected >= 50 subskills, got {len(subskills)}"

    seeds = [101, 102, 103]
    total_runs = 0
    synthetic_tokens = ["(Option", "(Alt", "(Alternative", "(Variation", "(Tier"]

    for seed in seeds:
        for idx, sub in enumerate(subskills):
            total_runs += 1
            res = generate(seed=seed, subskill=sub, count=1)
            assert len(res) == 1, f"Expected 1 item, got {len(res)}"
            item = res[0]

            prompt = item.get("prompt", "")
            opts = item.get("options", [])
            correct = item.get("correct_answer", "")
            hints = item.get("hints", {})

            # Assert 4 distinct options
            assert len(opts) == 4, f"Subskill {sub} seed {seed} does not have 4 options: {opts}"
            assert len(set(opts)) == 4, f"Subskill {sub} seed {seed} has duplicate options: {opts}"
            assert correct in opts, f"Subskill {sub} seed {seed} correct answer '{correct}' not in options: {opts}"

            # Assert hints
            assert hints.get("tier_1"), f"Subskill {sub} missing tier_1 hint"
            assert hints.get("tier_2"), f"Subskill {sub} missing tier_2 hint"
            assert hints.get("tier_3"), f"Subskill {sub} missing tier_3 hint"

            # Assert no synthetic tokens
            for opt in opts:
                for syn in synthetic_tokens:
                    assert syn not in opt, f"Subskill {sub} seed {seed} contains synthetic token '{syn}' in option '{opt}'"

            # Check no raw LaTeX leaks in options or prompt
            for latex_token in [r"\frac", r"\times", r"\text{"]:
                assert latex_token not in prompt, f"Prompt contains raw LaTeX: {latex_token} in {prompt}"
                for opt in opts:
                    assert latex_token not in opt, f"Option contains raw LaTeX: {latex_token} in {opt}"

    print(f"SUCCESS: All {total_runs} runs passed across {len(seeds)} seeds with 0 failures!")
    print("Zero synthetic distractors detected.")
    print("Zero duplicate choices detected.")
    print("Zero raw LaTeX leaks detected.")

if __name__ == "__main__":
    main()
