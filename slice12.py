import os

filename = 'src/components/workspace/registry/grade12Registry.js'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find("if (workspaceMode.includes('grade12_accounting_') && workspaceMode.endsWith('_practice')) {")
if idx != -1:
    end_idx = content.find("return null;", idx)
    if end_idx != -1:
        content = content[:idx] + content[end_idx:]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Removed Grade 12 Accounting Practice block")
