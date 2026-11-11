import os
import glob
import re

mathlit_dir = 'caps-ai-backend/app/utils/mathematical_literacy'
py_files = glob.glob(f'{mathlit_dir}/**/*.py', recursive=True)

print(f'Scanning {len(py_files)} files in {mathlit_dir}...')
for f in py_files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        lines = fp.readlines()
    for idx, line in enumerate(lines, 1):
        if 'replace(",", " ")' in line or "replace(',', ' ')" in line:
            print(f'{f}:{idx}: Comma replace: {line.strip()[:100]}')
        if '{ }' in line:
            print(f'{f}:{idx}: Literal {{ }}: {line.strip()[:100]}')
        if '7{,}50' in line or '7{ }50' in line:
            print(f'{f}:{idx}: 7.50 pattern: {line.strip()[:100]}')
