import os
import re

svgs = [
    "HumanEarSvg.jsx",
    "AlveolusGasExchangeSvg.jsx",
    "IntestinalVillusSvg.jsx",
    "MitosisStagesSvg.jsx",
    "MeiosisCrossingOverSvg.jsx",
    "EndocrineSystemSvg.jsx",
    "TransverseWaveSvg.jsx"
]

for s in svgs:
    p = os.path.join("src/components/workspace/modalities/diagram_bank", s)
    c = open(p, encoding='utf-8').read()
    testids = re.findall(r'data-testid="([^"]+)"', c)
    print(f"{s} -> {testids}")
