import xml.etree.ElementTree as ET
import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")

def inspect(fname):
    print(f"\n=== {fname} ===")
    tree = ET.parse(os.path.join(source_dir, fname))
    root = tree.getroot()
    for child in root:
        tag = child.tag.split('}')[-1]
        cid = child.attrib.get('id', '')
        clabel = child.attrib.get('{http://www.inkscape.org/namespaces/inkscape}label', '')
        print(f"Child <{tag}> id='{cid}' label='{clabel}'")

inspect("male_sagittal_vector.svg")
inspect("female_front_1_vector.svg")
