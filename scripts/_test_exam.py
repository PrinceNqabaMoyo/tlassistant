import sys, os, json
sys.path.insert(0, os.path.join("caps-ai-backend"))
from app.utils import bs_docs_harvester as H

print("import OK")
# term lookup
for k in ["grade10_bs_micro_environment", "grade10_bs_self_management",
          "grade11_bs_influences_on_business_environments"]:
    g = int(k[5:7])
    print(k, "term=", H._topic_term(k), "distinctive=", sorted(H._distinctive_tokens(k)))

print("\n--- which files feed grade10 micro_environment ---")
tt, et, sc = H._load_sources(10, "grade10_bs_micro_environment")
print("topic texts:", len(tt), "exam texts:", len(et), "sidecar:", sc is not None)

print("\n--- harvest_items counts per topic (Term1 example) ---")
items = H.harvest_items(10, "grade10_bs_micro_environment")
mcq = [i for i in items if i.get("kind") == "mcq"]
typed = [i for i in items if i.get("kind") != "mcq"]
print(f"micro_environment: typed={len(typed)} mcq={len(mcq)}")
for i in mcq[:3]:
    print("  MCQ:", i["prompt"][:70], "-> correct:", i["correct"], "idx", i["correct_index"])
for i in typed[:3]:
    print("  TYP:", i["prompt"][:70], "| memo pts:", len(i.get("marking_points", [])))
