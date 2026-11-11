content = open("src/components/workspace/UniversalWorkspace.jsx", encoding="utf-8").read()

for comp in ['<GeometricNets3DViewer', '<OrganicChemistry3DViewer', '<ElectrodynamicsMotorViewer']:
    pos = content.find(comp)
    if pos != -1:
        start = max(0, pos - 100)
        end = min(len(content), pos + 300)
        print(f"=== {comp} ===")
        print(content[start:end])
        print("...\n")
    else:
        print(f"NOT FOUND: {comp}")
