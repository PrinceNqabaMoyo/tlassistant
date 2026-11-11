import xml.etree.ElementTree as ET

tree = ET.parse("public/diagrams/human_ear_wikimedia.svg")
root = tree.getroot()
for el in root.iter():
    cid = el.attrib.get('id')
    if cid in ['rect7140', 'rect7136', 'rect7110', 'rect7159', 'rect9528', 'rect9531']:
        print(cid, el.attrib.get('style'))
