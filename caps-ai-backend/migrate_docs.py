import os
import re
from pathlib import Path

def sanitize_markdown(content):
    # Basic sanitization: ensure consistent heading spacing, remove multiple empty lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content

def migrate():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(base_dir, 'curriculum_docs')
    dest_dir = os.path.join(base_dir, 'caps-wiki')
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.md'):
                src_path = os.path.join(root, file)
                
                # Determine subject and grade from the path
                # Path looks like: .../curriculum_docs/BusinessStudies_Gr11/Term 1/file.md
                rel_path = os.path.relpath(src_path, src_dir)
                parts = Path(rel_path).parts
                
                if len(parts) >= 2:
                    subject_grade = parts[0] # e.g., BusinessStudies_Gr11
                    if '_' not in subject_grade:
                        continue
                        
                    subject_raw, grade_raw = subject_grade.split('_', 1)
                    subject_raw = subject_raw.strip()
                    grade_raw = grade_raw.strip()
                    
                    # Format subject: BusinessStudies -> business-studies, EMS -> ems
                    if subject_raw == 'BusinessStudies':
                        subject = 'business-studies'
                    elif subject_raw == 'EMS':
                        subject = 'ems'
                    elif subject_raw == 'Accounting':
                        subject = 'accounting'
                    else:
                        subject = subject_raw.lower()
                        
                    # Format grade: Gr11 -> grade-11
                    grade = grade_raw.lower().replace('gr', 'grade-')
                    
                    # Form destination dir
                    target_dir = os.path.join(dest_dir, subject, grade)
                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)
                    
                    # The file name will be lowercase, spaces replaced with dashes
                    base_name = os.path.splitext(file)[0].lower().replace(' ', '-')
                    # If it's deep in a term folder, prepend the term to avoid collisions
                    if len(parts) > 2:
                        term_folder = parts[-2].lower().replace(' ', '-')
                        if 'term' in term_folder:
                             base_name = f"{term_folder}-{base_name}"
                    
                    target_file = os.path.join(target_dir, f"{base_name}.md")
                    
                    # Read, sanitize, write
                    with open(src_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        
                    cleaned_content = sanitize_markdown(content)
                    
                    with open(target_file, 'w', encoding='utf-8') as f:
                        f.write(cleaned_content)
                    print(f"Migrated: {rel_path} -> {subject}/{grade}/{base_name}.md")

if __name__ == '__main__':
    migrate()
    print("Migration complete.")
