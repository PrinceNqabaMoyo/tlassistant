import xml.etree.ElementTree as ET
import os

source_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates", "female_scheme.svg")
tree = ET.parse(source_path)
root = tree.getroot()

# Check paths that have stroke="#000000" or black stroke
for i, path in enumerate(root.iter('{http://www.w3.org/2000/svg}path')):
    style = path.attrib.get('style', '')
    stroke = path.attrib.get('stroke', '')
    pid = path.attrib.get('id', '')
    if 'stroke:#000000' in style or stroke == '#000000' or stroke == '#000':
        print(f"Path id={pid}, style={style[:60]}")
