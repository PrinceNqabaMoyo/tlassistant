import json

with open('fundile-architecture.json', 'r', encoding='utf-8') as f:
    arch = json.load(f)

print("_meta:", json.dumps(arch.get('_meta'), indent=2))
