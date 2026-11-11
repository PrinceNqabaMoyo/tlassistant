import xml.etree.ElementTree as ET

# Clean eye SVG
tree = ET.parse("public/diagrams/human_eye_wikimedia.svg")
root = tree.getroot()

# Remove layer1 (Background) and layer18 (Single background)
to_remove = []
for child in root:
    gid = child.attrib.get('id')
    label = child.attrib.get('{http://www.inkscape.org/namespaces/inkscape}label')
    if gid in ['layer1', 'layer18'] or label in ['Background', 'Single background']:
        to_remove.append(child)

for elem in to_remove:
    root.remove(elem)
    print("Removed layer:", elem.attrib.get('id'), elem.attrib.get('{http://www.inkscape.org/namespaces/inkscape}label'))

tree.write("public/diagrams/human_eye_cleaned.svg", encoding="utf-8", xml_declaration=True)
print("Saved public/diagrams/human_eye_cleaned.svg")
