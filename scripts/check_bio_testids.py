content = open("src/components/workspace/modalities/BioDiagramModalityRenderer.jsx", encoding="utf-8").read()
import re
print("Found in BioDiagramModalityRenderer:")
for t in ["human-ear-canvas", "alveolus-gas-exchange-canvas", "intestinal-villus-canvas", "mitosis-stages-canvas", "meiosis-crossing-over-canvas", "endocrine-system-canvas", "transverse-wave-canvas"]:
    print(f"  {t}: {t in content}")
