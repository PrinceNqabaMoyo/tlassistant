import os
import re
from collections import Counter

qtypes = Counter()
modalities = Counter()
diagram_topics = []
table_topics = []
drag_drop_topics = []

for root, dirs, files in os.walk('caps-ai-backend/app/utils'):
    for f in files:
        if f.endswith('.py') and not f.startswith('__'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
                for m in re.finditer(r'["\']question_type["\']:\s*["\']([^"\']+)["\']', c):
                    qtypes[m.group(1)] += 1
                for m in re.finditer(r'["\']modality["\']:\s*["\']([^"\']+)["\']', c):
                    modalities[m.group(1)] += 1
                if 'diagram_spec' in c or 'diagram_select' in c or 'DiagramRenderer' in c or 'correct_edge' in c:
                    diagram_topics.append(f)
                if 'journal' in c or 'table_schema' in c or 'ledger' in c or 'correct_map' in c:
                    table_topics.append(f)
                if 'drag' in c.lower() or 'drop' in c.lower() or 'matching' in c.lower():
                    drag_drop_topics.append(f)

print('=== Emitted Question Types ===')
for k, v in qtypes.most_common():
    print(f'  {k}: {v}')

print('\n=== Emitted Modalities ===')
for k, v in modalities.most_common():
    print(f'  {k}: {v}')

print(f'\n=== Files with Diagram Spec / Diagram Select ({len(diagram_topics)}) ===')
for f in sorted(set(diagram_topics)):
    print(f'  {f}')

print(f'\n=== Files with Table / Journal / Ledger ({len(table_topics)}) ===')
print(f'  Total unique generator files: {len(set(table_topics))}')
for f in sorted(set(table_topics))[:15]:
    print(f'  {f}')

print(f'\n=== Files mentioning Drag / Drop / Matching ({len(drag_drop_topics)}) ===')
print(f'  Total unique files: {len(set(drag_drop_topics))}')
for f in sorted(set(drag_drop_topics))[:15]:
    print(f'  {f}')
