import xml.etree.ElementTree as ET
import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")

for fname in ["male_internal_organs.svg", "male_genitalia_internal.svg"]:
    tree = ET.parse(os.path.join(source_dir, fname))
    root = tree.getroot()
    print(f"=== {fname} ===")
    texts = [t.text for t in root.iter('{http://www.w3.org/2000/svg}text') if t.text]
    tspan = [t.text for t in root.iter('{http://www.w3.org/2000/svg}tspan') if t.text]
    all_t = set(texts + tspan)
    print("Labels count:", len(all_t))
    print("Labels:", list(all_t)[:15])
