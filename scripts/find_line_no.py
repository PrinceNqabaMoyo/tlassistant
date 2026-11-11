content = open("src/components/workspace/UniversalWorkspace.jsx", encoding="utf-8").read()
pos = content.find("setActiveSidecarAidId('aid_geometric_nets_3d')")
line_no = content[:pos].count('\n') + 1
print(f"Line number: {line_no}")
lines = content.splitlines()
for l in lines[max(0, line_no - 15):min(len(lines), line_no + 15)]:
    print(l)
