content = open("src/components/workspace/modalities/OrganicChemistry3DViewer.jsx", encoding="utf-8").read()
# Find props
for l in content.splitlines()[:120]:
    if 'function OrganicChemistry' in l or 'export default' in l or 'props' in l:
        print(l)
print("Keys in MOLECULES:", list(content.split("const MOLECULES = {")[1].split("};")[0]))
