import sys
import glob

files = [
    r'C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\app\utils\grade11_accounting\reconciliation_generator.py',
    r'C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\app\utils\grade11_accounting\fixed_assets_generator.py',
    r'C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\app\utils\grade11_accounting\partnership_ledger_generator.py',
    r'C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\app\utils\grade11_accounting\partnership_balance_sheet_generator.py'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to change:
    #         if show_answers:
    #             display = vals
    #         else:
    #             ...
    #             display = [
    # To just use the 'else' branch logic.
    
    # Pattern is a bit different in some files, let's do a careful replacement.
    if "if show_answers:" in content:
        # replace block
        old_block = """        if show_answers:
            display = vals
        else:
            editable_set = set(int(c) for c in editable_cols)
            display = [
                ("" if int(cix) in editable_set else ("" if v0 is None else str(v0)))
                for cix, v0 in enumerate(vals)
            ]"""
        
        new_block = """        editable_set = set(int(c) for c in editable_cols)
        display = [
            ("" if int(cix) in editable_set else ("" if v0 is None else str(v0)))
            for cix, v0 in enumerate(vals)
        ]"""
        
        content = content.replace(old_block, new_block)

        # partnership_balance_sheet_generator.py has a comment in the else block:
        old_block_2 = """        if show_answers:
            display = vals
        else:
            # In practice mode we must keep the table structure (labels, headings, given values)
            # and blank only the learner input cells.
            display = [
                ("" if int(cix) in set(editable_cols) else ("" if v0 is None else str(v0)))
                for cix, v0 in enumerate(vals)
            ]"""
        
        new_block_2 = """        editable_set = set(int(c) for c in editable_cols)
        display = [
            ("" if int(cix) in editable_set else ("" if v0 is None else str(v0)))
            for cix, v0 in enumerate(vals)
        ]"""
        content = content.replace(old_block_2, new_block_2)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Patched scaffold answer leakage in _mk_journal across all 4 files.")
