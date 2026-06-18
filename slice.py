import os

files = [
    'src/components/workspace/registry/grade10Registry.js',
    'src/components/workspace/registry/grade11Registry.js'
]

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
        
    # Remove practice imports
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if 'import Grade' in line and 'Practice ' in line and 'accounting' in line.lower():
            continue
        new_lines.append(line)
        
    content = '\n'.join(new_lines)
    
    # Remove practice blocks
    topics = ['indigenous', 'ethics', 'gaap', 'internal_control', 'sole_trader', 'accounting_scaffold'] # grade 11 has just accounting_scaffold? Or is it something else?
    
    # We will search for "if (workspaceMode === 'grade10_accounting_..._practice') {"
    # Since these chunks are always structured similarly, and end with "    }\n\n    return null;" or similar, we will find the start, then find the matching closing brace.
    while True:
        idx = content.find("if (workspaceMode === 'grade10_accounting_")
        if idx == -1: idx = content.find("if (workspaceMode === 'grade11_accounting_")
        if idx == -1: break
        
        # Check if it has _practice
        end_idx = content.find("') {", idx)
        tag = content[idx:end_idx+4]
        
        if '_practice' in tag:
            # find start of line
            start_line = content.rfind('\n', 0, idx)
            # find matching brace
            brace_count = 0
            found_first = False
            i = end_idx
            while i < len(content):
                if content[i] == '{':
                    brace_count += 1
                    found_first = True
                elif content[i] == '}':
                    brace_count -= 1
                
                i += 1
                if found_first and brace_count == 0:
                    break
            
            end_line = content.find('\n', i)
            if end_line == -1: end_line = len(content)
            
            content = content[:start_line] + content[end_line:]
        else:
            # Move on so we don't infinite loop. We hide the start temporally
            content = content[:idx] + "IF_WM_SC" + content[idx+18:]

    # Restore the hidden tags
    content = content.replace("IF_WM_SC", "if (workspaceMode ===")
    
    if content != original:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Refactored {filename}")
    else:
        print(f"Skipped {filename}")
