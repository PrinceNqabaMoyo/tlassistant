content = open("src/components/workspace/shared/mathx/DiagramRenderer.jsx", encoding="utf-8").read()
pos = content.find("circle_subtended_angle")
line_no = content[:pos].count('\n') + 1
lines = content.splitlines()
for l in lines[max(0, line_no - 10):min(len(lines), line_no + 50)]:
    print(l)
