import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")

with open(os.path.join(source_dir, "female_front_1_vector.svg"), "r", encoding="utf-8") as f:
    f_content = f.read()

idx = f_content.find("11189")
print("11189 index:", idx)
if idx != -1:
    print("Around 11189:", f_content[idx-30:idx+40])

with open(os.path.join(source_dir, "male_sagittal_vector.svg"), "r", encoding="utf-8") as f:
    m_content = f.read()

import xml.etree.ElementTree as ET
tree_m = ET.parse(os.path.join(source_dir, "male_sagittal_vector.svg"))
main_g_m = tree_m.getroot().find('{http://www.w3.org/2000/svg}g')
child_152 = list(main_g_m)[152]
print("Male Child 152 attrib:", child_152.attrib)
