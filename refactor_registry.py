import re
import os

files_to_process = [
    'src/components/workspace/registry/grade10Registry.js',
    'src/components/workspace/registry/grade11Registry.js'
]

for filename in files_to_process:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    print(f"Processing {filename}...")

    # 1. Replace availableModes
    content = content.replace("availableModes: ['scaffold', 'practice']", "availableModes: ['scaffold', 'marking']")
    content = content.replace("availableModes: ['scaffold', 'practice', 'marking']", "availableModes: ['scaffold', 'marking']")

    # 2. Modify scaffold conditions to include marking
    # e.g. if (workspaceMode === 'grade10_accounting_ethics_scaffold') {
    content = re.sub(
        r"if\s*\(\s*workspaceMode\s*===\s*'((?:grade10|grade11)_accounting_[a-zA-Z0-9_\-]+)_scaffold'\s*\)\s*\{",
        r"if (workspaceMode === '\1_scaffold' || workspaceMode === '\1_marking') {",
        content
    )

    # 3. Inject isMarkingEnv prop into the Scaffold components.
    # Looking for h(Grade10Accounting...Scaffold, {
    content = re.sub(
        r"(h\(\s*Grade(?:10|11)Accounting[a-zA-Z0-9]+Scaffold\s*,\s*\{)",
        r"\1\n            isMarkingEnv: workspaceMode.endsWith('_marking'),",
        content
    )

    # 4. Remove all Practice component imports for accounting
    content = re.sub(r"import\s+Grade(?:10|11)Accounting[a-zA-Z0-9]+Practice\s+from\s+[^;]+;\n?", "", content)

    # 5. Remove all the practice if blocks for accounting
    # Using a non-greedy dot to match everything up to the expected end of the block.
    # The block ends usually with a return statement, and then a closing brace at the same indentation level (4 spaces).
    # We can match `    if (workspaceMode === '..._practice') {`
    # up to `\n    }\n` or `\r\n    }\r\n`
    pattern_practice = r"    if\s*\(\s*workspaceMode\s*===\s*'(?:grade10|grade11)_accounting_[a-zA-Z0-9_\-]+_practice'\s*\)\s*\{.*?\n    \}\n"
    content = re.sub(pattern_practice, "", content, flags=re.DOTALL)

    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully updated {filename}")
    else:
        print(f"No changes made to {filename}")

