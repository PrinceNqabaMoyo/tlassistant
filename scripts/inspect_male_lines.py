import xml.etree.ElementTree as ET
import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")
tree = ET.parse(os.path.join(source_dir, "male_internal_organs.svg"))
root = tree.getroot()

# Check lines and polygons at the end of the file
for i, child in enumerate(root):
    tag = child.tag.split('}')[-1]
    if tag in ['line', 'polygon', 'text']:
        print(f"Child {i}: <{tag}> attrib={child.attrib}")
