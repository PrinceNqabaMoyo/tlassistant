import xml.etree.ElementTree as ET
import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")
diagrams_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams")

# 1. Clean female
tree_f = ET.parse(os.path.join(source_dir, "female_front_1_vector.svg"))
root_f = tree_f.getroot()
main_g_f = root_f.find('{http://www.w3.org/2000/svg}g')

# Remove children from index 44 to the end (pointer lines and text glyphs)
children_to_remove_f = list(main_g_f)[44:]
print(f"Removing {len(children_to_remove_f)} elements from female SVG...")
for child in children_to_remove_f:
    main_g_f.remove(child)

out_f_svg = os.path.join(diagrams_dir, "female_reproductive_cleaned.svg")
tree_f.write(out_f_svg, encoding='utf-8', xml_declaration=True)
print(f"Saved {out_f_svg}")


# 2. Clean male
tree_m = ET.parse(os.path.join(source_dir, "male_sagittal_vector.svg"))
root_m = tree_m.getroot()
main_g_m = root_m.find('{http://www.w3.org/2000/svg}g')

# Remove children from index 152 to the end (pointer lines and text glyphs)
children_to_remove_m = list(main_g_m)[152:]
print(f"Removing {len(children_to_remove_m)} elements from male SVG...")
for child in children_to_remove_m:
    main_g_m.remove(child)

out_m_svg = os.path.join(diagrams_dir, "male_reproductive_cleaned.svg")
tree_m.write(out_m_svg, encoding='utf-8', xml_declaration=True)
print(f"Saved {out_m_svg}")
