import xml.etree.ElementTree as ET
import re

tree = ET.parse('animal_cell_raw.svg')
root = tree.getroot()
print('Root tag:', root.tag)
print('Children count:', len(list(root)))
for idx, child in enumerate(root):
    tag = child.tag.split('}')[-1]
    cid = child.attrib.get('id', '')
    print(f'Child {idx}: <{tag}> id="{cid}"')

with open('animal_cell_raw.svg', 'r', encoding='utf-8') as f:
    raw_text = f.read()

text_tags = len(re.findall(r'<text\b', raw_text))
print('Total <text> tags:', text_tags)
