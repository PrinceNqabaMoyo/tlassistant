import xml.etree.ElementTree as ET

tree = ET.parse("public/diagrams/human_ear_wikimedia.svg")
root = tree.getroot()
ear_layer = None
for g in root.iter('{http://www.w3.org/2000/svg}g'):
    if g.attrib.get('id') == 'layer1':
        ear_layer = g
        break

if ear_layer is not None:
    for i, child in enumerate(ear_layer):
        tag = child.tag.split('}')[-1]
        cid = child.attrib.get('id')
        style = child.attrib.get('style', '')
        fill = child.attrib.get('fill', '')
        print(f"Child {i}: <{tag}> id={cid}, fill={fill}, style={style[:60]}")
