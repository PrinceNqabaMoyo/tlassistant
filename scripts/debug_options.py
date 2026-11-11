import sys
sys.path.insert(0, "caps-ai-backend")
from app.utils.mathematical_literacy.gr11_weight_and_temperature_generator import generate, SUBSKILLS

for i in range(len(SUBSKILLS)):
    for seed in [101, 202, 303]:
        q = generate(archetype_index=i, seed=seed)[0]
        if len(q["options"]) != 4:
            print(f"FAILED on subskill {SUBSKILLS[i]} with seed {seed}: options = {q['options']}")
            sys.exit(1)

print("All subskills have exactly 4 options across all seeds!")
