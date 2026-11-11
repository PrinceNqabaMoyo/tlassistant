import xml.etree.ElementTree as ET

tree = ET.parse("public/diagrams/human_ear_wikimedia.svg")
root = tree.getroot()

# Find and remove rect7140 and rect7136 if present
ear_layer = None
for g in root.iter('{http://www.w3.org/2000/svg}g'):
    if g.attrib.get('id') == 'layer1':
        ear_layer = g
        break

if ear_layer is not None:
    to_remove = []
    for c in ear_layer:
        cid = c.attrib.get('id')
        if cid in ['rect7140', 'rect7136']:
            to_remove.append(c)
    for c in to_remove:
        ear_layer.remove(c)
        print("Removed from ear:", c.attrib.get('id'))

tree.write("public/diagrams/human_ear_cleaned.svg", encoding="utf-8", xml_declaration=True)
print("Saved public/diagrams/human_ear_cleaned.svg")
