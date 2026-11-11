import sys
sys.path.insert(0, "caps-ai-backend")
from app.utils.mathematical_literacy.gr11_weight_and_temperature_generator import generate, SUBSKILLS

print("Subskills count:", len(SUBSKILLS))
assert len(SUBSKILLS) == 52, f"Expected 52, got {len(SUBSKILLS)}"

for i in range(len(SUBSKILLS)):
    q = generate(archetype_index=i, seed=200 + i)[0]
    assert q["subskill"] == SUBSKILLS[i], f"Mismatch: {q['subskill']} vs {SUBSKILLS[i]}"
    assert len(q["options"]) == 4, f"Options not 4: {q['options']}"
    assert q["correct_answer"] in q["options"], f"Correct not in options: {q['correct_answer']}"
    for opt in q["options"]:
        assert "(Alt" not in opt and "(Option" not in opt, f"Synthetic distractor found: {opt}"

print("All 52 subskills generated successfully with 0 errors!")
