import os
import re

science_dirs = [
    'grade10_life_sciences',
    'life_sciences',
    'natural_sciences',
    'grade10_physical_sciences',
    'grade11_physical_sciences',
    'grade12_physical_sciences',
    'physical_sciences'
]

print("=== SCIENCE GENERATORS DEEP FEATURE AUDIT ===")

for d in science_dirs:
    p = os.path.join('caps-ai-backend/app/utils', d)
    if not os.path.exists(p):
        continue
    for f in os.listdir(p):
        if f.endswith('.py') and not f.startswith('__'):
            fpath = os.path.join(p, f)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
                
                features = []
                if 'diagram' in c.lower():
                    features.append('diagram_mention')
                if 'diagram_spec' in c:
                    features.append('**HAS_DIAGRAM_SPEC**')
                if 'punnett' in c.lower():
                    features.append('punnett_grid')
                if 'table' in c.lower() or 'tabular' in c.lower():
                    features.append('table_mention')
                if 'circuit' in c.lower():
                    features.append('circuit_mention')
                if 'graph' in c.lower() or 'curve' in c.lower() or 'ogive' in c.lower():
                    features.append('graph_mention')
                if 'fbd' in c.lower() or 'free body' in c.lower():
                    features.append('fbd_mention')
                if 'optical' in c.lower() or 'ray' in c.lower():
                    features.append('ray/optics')
                
                mods = set(re.findall(r'["\']modality["\']:\s*["\']([^"\']+)["\']', c))
                qts = set(re.findall(r'["\']question_type["\']:\s*["\']([^"\']+)["\']', c))
                
                if mods:
                    features.append(f"mods={list(mods)}")
                if qts:
                    features.append(f"qtypes={list(qts)}")
                    
                print(f"[{d}/{f}] -> {', '.join(features)}")
