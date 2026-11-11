import xml.etree.ElementTree as ET
import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")
tree = ET.parse(os.path.join(source_dir, "male_internal_organs.svg"))
root = tree.getroot()

text_nodes = list(root.iter('{http://www.w3.org/2000/svg}text'))
print(f"Total <text> nodes in male_internal_organs: {len(text_nodes)}")
for t in text_nodes:
    print(t.attrib, "".join(t.itertext()))
