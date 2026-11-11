import xml.etree.ElementTree as ET
import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")

def inspect_group_elements(fname):
    print(f"\n=== {fname} ===")
    tree = ET.parse(os.path.join(source_dir, fname))
    root = tree.getroot()
    # Check top-level elements of root/g
    main_g = root.find('{http://www.w3.org/2000/svg}g')
    for i, child in enumerate(main_g):
        cid = child.attrib.get('id', '')
        tag = child.tag.split('}')[-1]
        num_children = len(child)
        print(f"Child {i}: <{tag}> id='{cid}' len={num_children}")

inspect_group_elements("female_front_1_vector.svg")
inspect_group_elements("male_sagittal_vector.svg")
