import xml.etree.ElementTree as ET
import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")

def inspect_sub(fname):
    print(f"\n=== {fname} ===")
    tree = ET.parse(os.path.join(source_dir, fname))
    root = tree.getroot()
    # Find all g children of root
    for g in root.iter('{http://www.w3.org/2000/svg}g'):
        gid = g.attrib.get('id', '')
        glabel = g.attrib.get('{http://www.inkscape.org/namespaces/inkscape}label', '')
        # check if it has text or path
        has_text = any(t.text for t in g.iter('{http://www.w3.org/2000/svg}text') if t.text)
        print(f"Group id='{gid}' label='{glabel}' has_text={has_text}")

inspect_sub("female_front_1_vector.svg")
inspect_sub("male_sagittal_vector.svg")
