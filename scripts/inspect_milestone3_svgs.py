import xml.etree.ElementTree as ET

def examine_svg(filepath):
    print("=== EXAMINING:", filepath)
    tree = ET.parse(filepath)
    root = tree.getroot()
    # namespaces
    ns = {'svg': 'http://www.w3.org/2000/svg', 'inkscape': 'http://www.inkscape.org/namespaces/inkscape'}
    
    for g in root.iter('{http://www.w3.org/2000/svg}g'):
        label = g.attrib.get('{http://www.inkscape.org/namespaces/inkscape}label')
        gid = g.attrib.get('id')
        style = g.attrib.get('style')
        if label or gid:
            # count children
            children = list(g)
            print(f"Layer/Group: id={gid}, label='{label}', style='{style}', children_count={len(children)}")
            text_children = [c for c in g.iter('{http://www.w3.org/2000/svg}text')]
            if text_children:
                print(f"  -> WARNING: Found {len(text_children)} <text> elements in {gid} ('{label}')")

examine_svg("public/diagrams/human_eye_wikimedia.svg")
examine_svg("public/diagrams/human_ear_wikimedia.svg")
