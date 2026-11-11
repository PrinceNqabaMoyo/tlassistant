import xml.etree.ElementTree as ET
import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")

tree = ET.parse(os.path.join(source_dir, "female_scheme.svg"))
root = tree.getroot()
for g in root.iter('{http://www.w3.org/2000/svg}g'):
    gid = g.attrib.get('id', '')
    texts = [t.text for t in g.iter('{http://www.w3.org/2000/svg}text') if t.text]
    tspan = [t.text for t in g.iter('{http://www.w3.org/2000/svg}tspan') if t.text]
    all_t = set(texts + tspan)
    if all_t:
        print(f"female_scheme.svg group {gid}: {all_t}")
