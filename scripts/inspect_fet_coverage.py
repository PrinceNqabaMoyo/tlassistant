import json

with open("scripts/syllabus_audit_refined.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=" * 85)
print(f"{'FET Subject / Grade':<30} | {'ATP Items':<10} | {'Genuine':<10} | {'Proxy':<8} | {'Missing':<10} | {'Coverage %':<10}")
print("=" * 85)

for k, v in sorted(data.items()):
    if any(g in k for g in ["_Gr10", "_Gr11", "_Gr12"]):
        tot = v.get("total_atp_items", len(v.get("items", [])))
        items = v.get("items", [])
        genuine = sum(1 for item in items if item.get("status") == "genuine")
        proxy = sum(1 for item in items if item.get("status") == "proxy")
        missing = sum(1 for item in items if item.get("status") == "missing")
        pct = (genuine / tot * 100) if tot > 0 else 0
        print(f"{k:<30} | {tot:<10} | {genuine:<10} | {proxy:<8} | {missing:<10} | {pct:>8.1f}%")

print("=" * 85)
