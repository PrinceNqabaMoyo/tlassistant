import xml.etree.ElementTree as ET
import os

svg_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates", "female_organs_frontal_unlabeled.svg")
tree = ET.parse(svg_path)
root = tree.getroot()

for i, child in enumerate(root):
    tag = child.tag.split('}')[-1]
    cid = child.attrib.get('id', '')
    clabel = child.attrib.get('{http://www.inkscape.org/namespaces/inkscape}label', '')
    print(f"Child {i}: <{tag}> id='{cid}' inkscape:label='{clabel}'")
    if tag == 'g':
        for j, gchild in enumerate(child):
            gtag = gchild.tag.split('}')[-1]
            gid = gchild.attrib.get('id', '')
            glabel = gchild.attrib.get('{http://www.inkscape.org/namespaces/inkscape}label', '')
            print(f"  Subchild {j}: <{gtag}> id='{gid}' label='{glabel}'")
