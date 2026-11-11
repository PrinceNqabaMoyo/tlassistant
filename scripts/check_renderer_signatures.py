import os
import re

renderers = [
    "src/components/workspace/modalities/DiagramModalityRenderer.jsx",
    "src/components/workspace/modalities/GeometricNets3DViewer.jsx",
    "src/components/workspace/modalities/OrganicChemistry3DViewer.jsx",
    "src/components/workspace/modalities/ElectrodynamicsMotorViewer.jsx",
    "src/components/workspace/modalities/BioDiagramModalityRenderer.jsx",
    "src/components/workspace/modalities/CircuitModalityRenderer.jsx",
    "src/components/workspace/modalities/FbdModalityRenderer.jsx"
]

for r in renderers:
    if os.path.exists(r):
        content = open(r, encoding='utf-8').read()
        testids = re.findall(r'data-testid="([^"]+)"', content)
        print(f"\n[{r}]")
        print(f"  test-ids: {set(testids)}")
        # Check first 200 chars or props
        props_match = re.search(r'export default function \w+\(([^)]*)\)', content)
        if props_match:
            print(f"  props: {props_match.group(1)}")
    else:
        print(f"MISSING: {r}")
