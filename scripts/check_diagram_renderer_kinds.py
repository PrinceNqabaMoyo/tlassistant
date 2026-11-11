content = open("src/components/workspace/shared/mathx/DiagramRenderer.jsx", encoding="utf-8").read()
print("Length of DiagramRenderer:", len(content))

import re
kinds = re.findall(r"spec\.kind\s*===?\s*['\"]([^'\"]+)['\"]", content)
print("Kinds:", set(kinds))
for l in content.splitlines():
    if 'kind' in l:
        print(" ", l.strip())
