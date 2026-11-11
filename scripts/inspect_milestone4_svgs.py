import xml.etree.ElementTree as ET
import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")

for fname in os.listdir(source_dir):
    if fname.endswith(".svg"):
        fpath = os.path.join(source_dir, fname)
        try:
            tree = ET.parse(fpath)
            root = tree.getroot()
            texts = [elem.text for elem in root.iter() if elem.tag.endswith('text') and elem.text]
            tspan_texts = [elem.text for elem in root.iter() if elem.tag.endswith('tspan') and elem.text]
            all_text = set(texts + tspan_texts)
            layers = [elem.attrib.get('id') for elem in root.iter() if elem.attrib.get('id')]
            print(f"\n=== {fname} ===")
            print(f"Root tag: {root.tag}, attribs: {root.attrib.keys()}")
            print(f"Text count: {len(all_text)}")
            print(f"Sample texts: {list(all_text)[:10]}")
            print(f"Sample layer IDs: {layers[:10]}")
        except Exception as e:
            print(f"Error reading {fname}: {e}")
