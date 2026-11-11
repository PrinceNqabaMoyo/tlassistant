content = open("src/components/workspace/shared/mathx/DiagramRenderer.jsx", encoding="utf-8").read()
pos = content.find("spec.kind === 'triangle'")
line_no = content[:pos].count('\n') + 1
lines = content.splitlines()
for l in lines[max(0, line_no - 10):min(len(lines), line_no + 45)]:
    print(l)
