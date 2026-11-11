with open('animal_cell_raw.svg', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the start of child 55 (<switch)
idx = text.find('<switch')
if idx != -1:
    clean_svg = text[:idx] + '\n</svg>'
    with open('public/diagrams/animal_cell_clean.svg', 'w', encoding='utf-8') as f:
        f.write(clean_svg)
    print(f"Successfully wrote clean animal cell SVG (sliced at index {idx})")
else:
    print("Could not find <switch in text!")
