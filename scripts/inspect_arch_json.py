import json

with open('fundile-architecture.json', 'r', encoding='utf-8') as f:
    arch = json.load(f)

print("Top keys:", list(arch.keys()))
print("lastUpdated:", arch.get("lastUpdated"))

# Search for diagram or visual
def search_dict(d, path=""):
    if isinstance(d, dict):
        for k, v in d.items():
            search_dict(v, f"{path}.{k}" if path else k)
    elif isinstance(d, list):
        for idx, item in enumerate(d):
            search_dict(item, f"{path}[{idx}]")
    elif isinstance(d, str):
        if any(w in d.lower() for w in ["diagram", "modality", "archetype"]):
            print(f"{path}: {d[:80]}")

search_dict(arch)
