import os

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = {
        'Grade10AccountingFinalAccountsScaffold': 'EmsScaffold',
        'Grade10AccountingFinalAccountsPractice': 'EmsPractice',
        'Grade10Accounting': 'Ems',
        'useGrade10AccountingMarking': 'useEmsMarking',
        'g10AcctFAScaffold': 'scaffold',
        'g10AcctFAPractice': 'practice',
        'g10AcctFAVisualAidsOpen': 'visualAidsOpen',
        'setG10AcctFAVisualAidsOpen': 'setVisualAidsOpen',
        'g10AcctFA': 'ems',
        'fetchGrade10AcctFAScaffoldQuestion': 'fetchScaffoldQuestion',
        'fetchGrade10AcctFAPractice': 'fetchPractice',
        'renderGrade10AcctFAVisualAids': 'renderVisualAids',
        'Grade 10 Accounting • Final Accounts': 'Grade 7 EMS',
        'setG10AcctFAScaffold': 'setScaffold',
        'setG10AcctFAPractice': 'setPractice',
    }

    for old, new in replacements.items():
        content = content.replace(old, new)
        
    # Extra fix for capitalizations that might have been broken
    content = content.replace('setscaffold', 'setScaffold')
    content = content.replace('setpractice', 'setPractice')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"c:\Users\princ\fundile-tlassistant-vite\src\components\workspace\grade7\ems"
files = ["EmsScaffold.jsx", "EmsPractice.jsx", "useEmsMarking.jsx"]

for f in files:
    replace_in_file(os.path.join(base_dir, f))

print("Replacement complete.")
