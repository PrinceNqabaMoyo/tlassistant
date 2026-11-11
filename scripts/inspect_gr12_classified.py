import json

with open("reports/data/mathlit_audit_classified.json", "r", encoding="utf-8") as f:
    data = json.load(f)

missing = []
gnr = []
described = []
rendered = []
total_gr12 = 0

for key, item in data.items():
    if not (key.startswith("gr12_") or item.get("grade") == 12 or "grade12" in key):
        continue
    total_gr12 += 1
    status = item.get("classification")
    sid = item.get("subskill_id", key)
    topic = item.get("topic")
    failures = item.get("failures", [])
    if status == "MISSING":
        missing.append((topic, sid, failures))
    elif status == "GNR":
        gnr.append((topic, sid, failures, item.get("diagram_spec_kind")))
    elif status == "DESCRIBED_NOT_DRAWN":
        described.append((topic, sid, item.get("figure_refs", [])))
    elif status == "RENDERED":
        rendered.append(sid)

print(f"Total Gr12: {total_gr12}")
print(f"Counts: RENDERED={len(rendered)}, MISSING={len(missing)}, GNR={len(gnr)}, DESCRIBED={len(described)}")

print(f"\n--- DESCRIBED ({len(described)}) ---")
for t, s, refs in described:
    print(f"[{t}] {s}: refs={refs}")

print(f"\n--- GNR ({len(gnr)}) ---")
for t, s, fails, kind in gnr:
    print(f"[{t}] {s} (kind={kind}): {fails}")

print(f"\n--- MISSING ({len(missing)}) ---")
for t, s, fails in missing:
    print(f"[{t}] {s}: {fails}")
