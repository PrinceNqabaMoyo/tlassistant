import json

with open('fundile-architecture.json', 'r', encoding='utf-8') as f:
    arch = json.load(f)

print("Built components count:", len(arch['frontendComponents']['built']))
print("Built generators count:", len(arch['generators']['built']))

# Look for diagram or modality in built components
diag_comps = [c for c in arch['frontendComponents']['built'] if any(w in str(c).lower() for w in ['diagram', 'modality', 'svg', 'canvas'])]
print(f"Diagram components in frontendComponents.built: {len(diag_comps)}")
for dc in diag_comps:
    print(" ", dc.get('name') if isinstance(dc, dict) else dc)
