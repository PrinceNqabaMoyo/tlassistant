content = open("src/components/workspace/modalities/OrganicChemistry3DViewer.jsx", encoding="utf-8").read()
idx = content.find("export default function")
print(content[idx:idx+300])
