import re

content = open("src/components/workspace/modalities/OpticsRayModalityRenderer.jsx", encoding="utf-8").read()
print("OpticsRay test-ids:", re.findall(r'data-testid="([^"]+)"', content))
