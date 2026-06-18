import re

def check_file(path):
    data = open(path, encoding='utf-8').read()
    blocks = data.split('_make_fill_in_table_question')
    print(f"Checking {path}, found {len(blocks)-1} families")
    for i, b in enumerate(blocks[1:]):
        m = re.search(r'\),\s*[\"\'\']([a-zA-Z0-9_]+)[\"\'\']', b)
        if not m:
            m = re.search(r'\"([a-zA-Z0-9_]+_fill)\"', b)
        if m:
            family = m.group(1)
            if 'cell_teaching_map' not in b:
                print('Missing:', family)
        else:
            print(f"Could not parse family name in block {i}")

check_file(r'caps-ai-backend\app\utils\grade10_accounting\term2\final_accounts_generator\adjustment_families.py')
check_file(r'caps-ai-backend\app\utils\grade10_accounting\term2\final_accounts_generator\core_families.py')
