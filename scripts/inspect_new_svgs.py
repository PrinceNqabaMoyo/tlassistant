import xml.etree.ElementTree as ET
import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")

files = [
    "male_sagittal_vector.svg",
    "male_human_repro_vector.svg",
    "female_front_1_vector.svg",
    "female_internal_unlabeled.svg",
    "female_no_description.svg",
]

for fname in files:
    fpath = os.path.join(source_dir, fname)
    tree = ET.parse(fpath)
    root = tree.getroot()
    texts = [t.text for t in root.iter('{http://www.w3.org/2000/svg}text') if t.text]
    tspans = [t.text for t in root.iter('{http://www.w3.org/2000/svg}tspan') if t.text]
    all_t = set(texts + tspans)
    print(f"\n=== {fname} ===")
    print(f"Total texts: {len(all_t)}")
    if all_t:
        print("Sample texts:", list(all_t)[:5])
    else:
        print("COMPLETELY 100% UNLABELED!")
