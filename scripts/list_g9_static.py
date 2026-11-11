import sys
from pathlib import Path

ROOT = Path(".")
sys.path.insert(0, str(ROOT / "caps-ai-backend"))

from app.services.caps_term_curriculum_registry import _ALL_TOPIC_RECORDS
from app.services.generator_registry import generate_variant, get_topic_archetypes

g9 = [t for t in _ALL_TOPIC_RECORDS if str(t.get("grade")) == "9"]

static_list = []
for t in g9:
    subj = t.get("subject")
    name = t.get("name")
    archs = get_topic_archetypes(topic=name, grade="9", subject=subj).get("archetypes") or []
    for a in archs:
        try:
            q1 = generate_variant(name, subskill=a, grade="9", subject=subj, seed=101)[0]
            q2 = generate_variant(name, subskill=a, grade="9", subject=subj, seed=202)[0]
            q3 = generate_variant(name, subskill=a, grade="9", subject=subj, seed=303)[0]
            if q1.get("prompt") == q2.get("prompt") == q3.get("prompt"):
                static_list.append((subj, name, a))
        except Exception as e:
            pass

print(f"Total static archetypes in Grade 9: {len(static_list)}")
from collections import defaultdict
grouped = defaultdict(list)
for s, n, a in static_list:
    grouped[(s, n)].append(a)

for (s, n), archs in grouped.items():
    print(f"{s} | {n} ({len(archs)} static): {archs}")
