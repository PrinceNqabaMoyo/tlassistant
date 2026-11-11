import json

with open('fundile-architecture.json', 'r', encoding='utf-8') as f:
    arch = json.load(f)

print("frontendComponents keys:", list(arch.get('frontendComponents', {}).keys()))
print("generators keys:", list(arch.get('generators', {}).keys()))
