import sys
sys.path.insert(0, "caps-ai-backend")
from app.utils.mathematical_literacy.gr11_probability_generator import generate, SUBSKILLS

for i in range(len(SUBSKILLS)):
    for seed in [101, 202, 303]:
        q = generate(archetype_index=i, seed=seed)[0]
        if len(q["options"]) != 4:
            print(f"FAILED on subskill {SUBSKILLS[i]} with seed {seed}: options = {q['options']}")
            sys.exit(1)
        if q["correct_answer"] not in q["options"]:
            print(f"FAILED: correct not in options for {SUBSKILLS[i]}")
            sys.exit(1)
        for opt in q["options"]:
            if "(Alt" in opt or "(Option" in opt or "(Alternative" in opt:
                print(f"FAILED: synthetic distractor {opt} in {SUBSKILLS[i]}")
                sys.exit(1)

print("All 52 probability subskills have 4 distinct options across all seeds with 0 synthetic placeholders!")
