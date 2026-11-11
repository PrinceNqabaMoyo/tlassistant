import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")
diagrams_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams")

with open(os.path.join(source_dir, "female_front_1_vector.svg"), "r", encoding="utf-8") as f:
    f_content = f.read()

idx_g10959 = f_content.find('id="g10959"')
# Find the '<g' immediately preceding it
start_f = f_content.rfind('<g', 0, idx_g10959)
end_f = f_content.rfind('</g>')
clean_f = f_content[:start_f] + f_content[end_f:]

out_f = os.path.join(diagrams_dir, "female_reproductive_cleaned.svg")
with open(out_f, "w", encoding="utf-8") as f:
    f.write(clean_f)
print(f"Cleaned female: {len(f_content)} -> {len(clean_f)} bytes")
