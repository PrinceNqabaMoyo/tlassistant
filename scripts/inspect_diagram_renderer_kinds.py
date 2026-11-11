with open('src/components/workspace/shared/mathx/DiagramRenderer.jsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'GeoGebraGeometryRenderer' in l or 'FunctionGraph' in l or 'StatsAndFinancialGraphRenderer' in l:
        print(f"L{i+1}: {l.strip()}")
