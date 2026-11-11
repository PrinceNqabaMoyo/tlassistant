import xml.etree.ElementTree as ET
import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")

def inspect_texts(fname):
    print(f"\n=== {fname} ===")
    with open(os.path.join(source_dir, fname), 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Search for words like "Bladder", "cervix", etc.
    for word in ["Bladder", "vas deferens", "cervix", "vagina", "ovary"]:
        idx = content.find(word)
        if idx != -1:
            print(f"Found '{word}' at index {idx}!")
            # print surrounding 200 chars
            print(content[max(0, idx-100):min(len(content), idx+100)])

inspect_texts("female_front_1_vector.svg")
inspect_texts("male_sagittal_vector.svg")
