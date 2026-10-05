"""
Script to generate mockschool.md directly from mockEnvironment datasets
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Read the files
with open(ROOT / 'src/data/mock/mockSchool.js', 'r', encoding='utf-8') as f:
    school_content = f.read()

with open(ROOT / 'src/data/mock/mockFaculty.js', 'r', encoding='utf-8') as f:
    faculty_content = f.read()

with open(ROOT / 'src/data/mock/mockSchoolStudents.js', 'r', encoding='utf-8') as f:
    school_students_content = f.read()

with open(ROOT / 'src/data/mock/mockIndependentStudents.js', 'r', encoding='utf-8') as f:
    ind_students_content = f.read()

with open(ROOT / 'src/data/mock/mockParents.js', 'r', encoding='utf-8') as f:
    parents_content = f.read()

print("Read all mock JS files successfully.")
