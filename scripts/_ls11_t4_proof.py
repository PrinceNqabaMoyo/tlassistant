"""Proof that the syllabus's LS Gr11 Term 4 topics are now harvestable.

The registry has ONE topic for Term 4 while the syllabus names FOUR (plus the
atmosphere/water split). This bypasses the registry by stubbing _topic_meta, so
each SYLLABUS topic name is put through the real source-selection path:
filename match -> chapter-section match -> textbook-PDF fallback.

Usage: python scripts/_ls11_t4_proof.py
"""
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps-ai-backend"))
from app.utils import sci_docs_harvester as S  # noqa: E402

SUBJECT, GRADE = "Life Sciences", 11
# term 4 as the syllabus states it, plus the two halves of its water topic
TOPICS = [
    (4, "Human impact on the environment"),
    (4, "The atmosphere and climate change"),
    (4, "Water availability"),
    (4, "Water quality"),
    (4, "Water Purification & Recycling"),
    (4, "Food Security"),
    (4, "Loss of Biodiversity"),
    (4, "Solid Waste Disposal"),
]


def probe(name, term):
    key = "probe_" + S._norm_name(name).replace(" ", "_")

    def fake(topic_key):
        if topic_key != key:
            return _real(topic_key)
        return (SUBJECT, GRADE, frozenset({term}), (name,))

    _real = S._topic_meta
    S._topic_meta = fake
    for fn in (S._load_all, S._candidate_files, S._section_sources):
        try:
            fn.cache_clear()
        except AttributeError:
            pass
    try:
        files = S._candidate_files(GRADE, key)
        texts, _side, used, rejected = S._load_all(GRADE, key)
        items = S.harvest_items(GRADE, key, limit=400)
        pairs = S.harvest_pairs(GRADE, key)
        mcq = len([i for i in items if i["kind"] == "mcq"])
        typed = len(items) - mcq
        memo = len([i for i in items if i.get("marking_points")])
    finally:
        S._topic_meta = _real
        for fn in (S._load_all, S._candidate_files, S._section_sources):
            try:
                fn.cache_clear()
            except AttributeError:
                pass
    return files, used, rejected, items, pairs, typed, mcq, memo


print(f"{'SYLLABUS TOPIC':38s} {'src':13s} {'files':5s} {'typed':5s} {'mcq':4s} "
      f"{'memo':4s} {'pairs':5s}")
print("-" * 92)
for term, name in TOPICS:
    files, used, rejected, items, pairs, typed, mcq, memo = probe(name, term)
    src = "none"
    if used:
        src = "section" if any("chapter section" in u for u in used) else (
            "PDF" if any("mined from PDF" in u for u in used) else "chapter .md")
    print(f"{name[:38]:38s} {src:13s} {len(files):<5d} {typed:<5d} {mcq:<4d} {memo:<4d} {len(pairs):<5d}")
    for u in used:
        print(f"       used  {u[:88]}")
    for r in rejected:
        print(f"       reject {r[:87]}")
    if items:
        print(f"       sample: {items[0]['prompt'][:96]!r}")
