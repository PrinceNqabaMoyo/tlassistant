import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")
diagrams_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams")

# 1. Female
with open(os.path.join(source_dir, "female_front_1_vector.svg"), "r", encoding="utf-8") as f:
    f_content = f.read()

idx_11189 = f_content.find('id="polyline11189"')
# Find the '<polyline' immediately preceding it
start_f = f_content.rfind('<polyline', 0, idx_11189)
end_f = f_content.rfind('</g>')
clean_f = f_content[:start_f] + f_content[end_f:]

out_f = os.path.join(diagrams_dir, "female_reproductive_cleaned.svg")
with open(out_f, "w", encoding="utf-8") as f:
    f.write(clean_f)
print(f"Cleaned female: {len(f_content)} -> {len(clean_f)} bytes")


# 2. Male
with open(os.path.join(source_dir, "male_sagittal_vector.svg"), "r", encoding="utf-8") as f:
    m_content = f.read()

idx_m_points = m_content.find('281.23 134.95 312.49 134.95')
start_m = m_content.rfind('<polyline', 0, idx_m_points)
end_m = m_content.rfind('</g>')
clean_m = m_content[:start_m] + m_content[end_m:]

out_m = os.path.join(diagrams_dir, "male_reproductive_cleaned.svg")
with open(out_m, "w", encoding="utf-8") as f:
    f.write(clean_m)
print(f"Cleaned male: {len(m_content)} -> {len(clean_m)} bytes")
