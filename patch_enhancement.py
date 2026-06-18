
import sys

filepath = r'C:\Users\princ\fundile-tlassistant-vite\gr11accounting-enhancement.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'Ensure that the initial cells sent to the student are either explicitly set to empty strings or 
ull, and that the expected answers are strictly hidden in the expectedMap or correct_map and not pre-populated in the view layer.',
    'Ensure that the initial cells sent to the student have SOME cells pre-filled (like account names or partial figures) to guide Grade 11 students, while the cells they are actually required to answer are empty strings. The expected answers for those blank cells must be strictly hidden in expectedMap.'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Patched enhancement plan')

