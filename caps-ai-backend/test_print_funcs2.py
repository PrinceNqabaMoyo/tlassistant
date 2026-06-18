import re

f = open('app/utils/grade11_accounting/fixed_assets_generator.py', encoding='utf-8').read()
funcs = re.findall(r'def _[a-zA-Z0-9_]+\(', f)
print('\n'.join(funcs))
