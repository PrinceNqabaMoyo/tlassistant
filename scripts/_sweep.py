import sys, os, json
sys.path.insert(0, os.path.join("caps-ai-backend"))
from app.utils import bs_docs_harvester as H

REG = os.path.join("caps-ai-backend", "app", "services", "caps_term_registry_data.json")
keys = [e["generator_key"] for e in json.load(open(REG, encoding="utf-8")) if "_bs_" in str(e.get("generator_key", ""))]
tot = 0; zero = []
print(f"{'topic_key':50} {'term':>4} {'typed':>5} {'mcq':>4} {'pairs':>5}")
for k in sorted(keys):
    g = int(k[5:7])
    items = H.harvest_items(g, k)
    pairs = H.harvest_pairs(g, k)
    typed = sum(1 for i in items if i.get("kind") != "mcq"); mcq = len(items) - typed
    tot += len(items)
    if len(items) == 0:
        zero.append(k)
    print(f"{k:50} {str(H._topic_term(k)):>4} {typed:>5} {mcq:>4} {len(pairs):>5}")
print("TOTAL items =", tot, "| zero-harvest topics =", zero)
# integrity check on mcq indices
bad = 0
for k in keys:
    for it in H.harvest_items(int(k[5:7]), k):
        if it.get("kind") == "mcq":
            try:
                ci = int(it["correct_index"]); assert 0 <= ci < len(it["options"]) and it["options"][ci] == it["correct"]
            except Exception:
                bad += 1
print("mcq integrity problems =", bad)
