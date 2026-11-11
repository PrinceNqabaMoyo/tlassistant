"""Report science questions whose text is actually Business Studies content."""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps-ai-backend"))
from app.utils import sci_docs_harvester as S

BUS = re.compile(
    r"business|micro environment|market environment|macro environment|entrepreneur"
    r"|stanp|cash book|ledger|debit|credit|\bvat\b|income statement|balance sheet"
    r"|stakeholder|swot|pestle|mark allocation|archetype", re.I,
)

seen, tot = set(), 0
for e in S._registry_rows():
    k = e["generator_key"]
    if k in seen:
        continue
    seen.add(k)
    its = S.harvest_items(None, k)
    hits = [i for i in its
            if BUS.search(str(i.get("prompt", "")) + " " + " ".join(i.get("marking_points") or []))]
    prs = [p for p in S.harvest_pairs(None, k) if BUS.search(p[0] + " " + p[1])]
    if hits or prs:
        tot += len(hits) + len(prs)
        print(f"{e['subject']} Gr{S._grade_of(None, k)}  {k}: items={len(hits)} pairs={len(prs)}")
        for i in hits[:2]:
            print("      Q   ", i["prompt"][:95])
        for t, d in prs[:2]:
            print(f"      PAIR {t[:38]} -> {d[:55]}")
print("=" * 70)
print("TOTAL CONTAMINATED SCIENCE ENTRIES =", tot)
