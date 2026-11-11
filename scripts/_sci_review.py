"""Per-topic extraction review for the science doc-harvester.

Usage:  python scripts/_sci_review.py "Life Sciences" 10
Prints, for every topic (generator_key) in a subject+grade: the source chapter
it drew from, item counts, and sample questions WITH their memo, so a human can
sign off the grade. Also flags sibling overlap (two topics harvesting the same
content) and empty topics.
"""
import sys, os, json, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps-ai-backend"))
from app.utils import sci_docs_harvester as S

REG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "caps-ai-backend", "app", "services", "caps_term_registry_data.json")


def topics(subject, grade):
    data = json.load(open(REG, encoding="utf-8"))
    out, seen = [], set()
    for e in data:
        if str(e.get("subject")) == subject and str(e.get("grade")) == str(grade):
            k = e["generator_key"]
            if k in seen:
                continue
            seen.add(k)
            out.append((k, e.get("term"), e.get("name")))
    return out


def sig(items, prs):
    blob = "|".join(sorted(
        [str(i.get("prompt", ""))[:120] for i in items] + [f"{t}={d[:60]}" for t, d in prs]))
    return hashlib.md5(blob.encode("utf-8")).hexdigest()[:12]


def show(k, term, name):
    items = S.harvest_items(None, k)
    prs = S.harvest_pairs(None, k)
    g = S._grade_of(None, k)
    typed = [i for i in items if i.get("kind") != "mcq"]
    mcq = [i for i in items if i.get("kind") == "mcq"]
    paths = S._load_all(g, k)[2]
    print("=" * 78)
    print(f"TOPIC  {k}   (term {term}) name={name!r}")
    print(f"COUNTS typed={len(typed)}  mcq={len(mcq)}  pairs={len(prs)}")
    print("SOURCES")
    for p in paths:
        print(f"    {p}")
    if not items:
        print("  !! NO ITEMS !!")
        return sig(items, prs), set(paths)
    for it in typed[:2]:
        print(f"  TYPED: {it['prompt'][:110]}")
        print(f"     memo: {it['marking_points'][:3]}")
    for it in mcq[:1]:
        print(f"  MCQ:   {it['prompt'][:110]}")
        print(f"     opts: {it['options']}  correct={it['correct']!r} idx={it['correct_index']}")
    for t, d in prs[:2]:
        print(f"  PAIR:  {t!r} -> {d[:80]}")
    return sig(items, prs), set(paths)


def main():
    subject = sys.argv[1] if len(sys.argv) > 1 else "Life Sciences"
    grade = sys.argv[2] if len(sys.argv) > 2 else "10"
    n = 0
    sigs, srcmap = {}, {}
    for k, term, name in topics(subject, grade):
        s, paths = show(k, term, name)
        sigs.setdefault(s, []).append(k)
        srcmap[k] = paths
    print("=" * 78)
    for s, ks in sigs.items():
        if len(ks) > 1:
            print(f"!! OVERLAP identical harvest: {ks}")
    allk = list(srcmap)
    for i in range(len(allk)):
        for j in range(i + 1, len(allk)):
            a, b = allk[i], allk[j]
            if srcmap[a] and srcmap[a] == srcmap[b]:
                print(f"!! SAME FILES: {a} <-> {b}")
    empty = [k for k in allk if not srcmap[k]]
    if empty:
        print(f"!! NO SOURCE FILES: {empty}")
    print(f"{subject} Gr{grade}: {len(allk)} topics reviewed. "
          f"distinct-signatures={len(sigs)}. clean={not any(len(v) > 1 for v in sigs.values())}")


if __name__ == "__main__":
    main()
