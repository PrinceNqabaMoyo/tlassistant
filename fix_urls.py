import os
import re

files_to_fix = [
    r"src\app\hooks\useWorkspaceSubmissionFlow.js",
    r"src\components\math\GeometryStudio.jsx",
    r"src\components\sourceDocuments\SourceDocumentRepository.jsx",
    r"src\components\teacher\AssessmentGenerator.jsx",
    r"src\components\workspace\grade10\accounting\useGrade10AccountingMarking.js",
    r"src\components\workspace\grade10\business-studies\useGrade10BusinessStudiesMarking.js",
    r"src\components\workspace\grade11\accounting\useGrade11AccountingMarking.js",
    r"src\components\workspace\grade11\business-studies\useGrade11BusinessStudiesMarking.js",
    r"src\components\workspace\grade11\business-studies\term-1\challenges-of-the-business-environments\controller.js",
    r"src\components\workspace\grade11\business-studies\term-1\influences-on-business-environments\controller.js",
    r"src\components\workspace\grade12\accounting\useGrade12AccountingMarking.js"
]

base_dir = r"C:\Users\princ\fundile-tlassistant-vite"

for rel_path in files_to_fix:
    full_path = os.path.join(base_dir, rel_path)
    if not os.path.exists(full_path):
        continue
        
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    orig_content = content
    
    # Fix the weird URL typo in Grade 10 Accounting
    content = content.replace("'https://snombi-tlassistant.hf.spacehttp://localhost:/api", "buildApiUrl('/api")
    
    # Replace direct string literals
    content = re.sub(r"'https://snombi-tlassistant\.hf\.space(/api/[^']+)'", r"buildApiUrl('\1')", content)
    
    # Fix controllers string templating
    content = content.replace("`https://snombi-tlassistant.hf.space${endpointPath}`", "buildApiUrl(endpointPath)")
    
    if content != orig_content:
        # Add import if missing
        if "buildApiUrl" not in orig_content:
            depth = len(rel_path.split('\\')) - 2
            if depth < 0: depth = 0
            import_path = '../' * depth + 'utils/apiBaseUrl'
            import_stmt = f"import {{ buildApiUrl }} from '{import_path}';\n"
            content = import_stmt + content
            
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {rel_path}")
