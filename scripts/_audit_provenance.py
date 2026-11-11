"""Provenance check for the 293 token-flagged items: every harvested term must
occur in the topic's OWN matched .md file(s); anything not found is a real leak."""
import sys, os, re, json
sys.path.insert(0, os.path.join("caps-ai-backend"))
from app.api import grade10_business_studies as g10
from app.api import grade11_business_studies as g11
from app.api import grade12_business_studies as g12
from app.utils import bs_docs_harvester as H

MODULES = {"grade10": g10, "grade11": g11, "grade12": g12}
SUBSKILLS = ["word_bank", "matching", "crossword"]

def answer_terms(q):
    t = q.get("question_type")
    if t == "word_bank": return list((q.get("correct_map") or {}).values())
    if t == "matching_columns": return list((q.get("correct_pairs") or {}).values())
    if t == "crossword": return list(q.get("words") or [])
    return []

total_flagged = 0
leaks = []
for gname, mod in MODULES.items():
    for topic, fn in mod.GENERATORS.items():
        gen = fn if callable(fn) and not hasattr(fn, "generate") else fn.generate
        rel = H._distinctive_tokens(topic) | {topic, gname}
        grade = int(topic[5:7])
        topic_texts, _exam, sidecar = H._load_sources(grade, topic)
        own = " ".join(topic_texts).lower() if topic_texts else (json.dumps(sidecar).lower() if sidecar else "")
        for sk in SUBSKILLS:
            try: qs = gen(subskill=sk, difficulty="medium", count=200, seed=42, topic=topic)
            except Exception: continue
            for q in qs:
                txt = json.dumps(q, default=str).lower()
                toks = set(re.sub(r"[^a-z0-9 ]", " ", txt).split())
                if toks & rel:
                    continue  # clearly on-topic by tokens
                total_flagged += 1
                for a in answer_terms(q):
                    if a and a.lower() not in own:
                        leaks.append((topic, sk, a))
print(f"flagged items checked = {total_flagged}")
uniq = sorted(set(leaks))
print(f"distinct term-level provenance leaks = {len(uniq)}")
for t, sk, a in uniq[:30]:
    print(f"  LEAK {t} [{sk}] term={a!r}")
