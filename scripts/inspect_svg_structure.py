import xml.etree.ElementTree as ET
import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")

def inspect_svg(fname):
    print(f"\n================= {fname} =================")
    fpath = os.path.join(source_dir, fname)
    tree = ET.parse(fpath)
    root = tree.getroot()
    
    # Check top-level elements and groups
    for i, child in enumerate(root):
        tag = child.tag.split('}')[-1]
        cid = child.attrib.get('id', '')
        cclass = child.attrib.get('class', '')
        print(f"Child {i}: <{tag}> id='{cid}' class='{cclass}'")
        if tag == 'g':
            for j, gchild in enumerate(child):
                gtag = gchild.tag.split('}')[-1]
                gid = gchild.attrib.get('id', '')
                if gtag in ['text', 'g'] or 'text' in gid.lower() or 'label' in gid.lower():
                    print(f"  Subchild {j}: <{gtag}> id='{gid}'")

inspect_svg("male_internal_organs.svg")
inspect_svg("female_scheme.svg")
