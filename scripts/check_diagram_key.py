import json

with open('fundile-architecture.json', 'r', encoding='utf-8') as f:
    arch = json.load(f)

for k in arch.keys():
    if 'diagram' in k.lower():
        print("Found key:", k)

if 'curriculumDiagrams' in arch:
    print("Found curriculumDiagrams")
