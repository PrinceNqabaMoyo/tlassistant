import re

with open('public/diagrams/animal_cell_clean.svg', 'r', encoding='utf-8') as f:
    s = f.read()

# Replace viewBox to crop cleanly around the cell
s = re.sub(r'viewBox="[^"]+"', 'viewBox="-40 -20 570 420"', s)

with open('public/diagrams/animal_cell_clean.svg', 'w', encoding='utf-8') as f:
    f.write(s)

print("Adjusted viewBox in animal_cell_clean.svg")
