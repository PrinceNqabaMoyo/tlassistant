import xml.etree.ElementTree as ET
import os

svg_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates", "female_organs_frontal_unlabeled.svg")
tree = ET.parse(svg_path)
root = tree.getroot()

image_elem = root.find('{http://www.w3.org/2000/svg}image')
print("Image attribs:", image_elem.attrib.keys())
href = image_elem.attrib.get('{http://www.w3.org/1999/xlink}href', '')
print("Image href starts with:", href[:50])
print("Image href length:", len(href))
