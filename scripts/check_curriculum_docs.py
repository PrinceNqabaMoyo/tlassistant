import os
import glob

search_dirs = [
    "curriculum_docs_auto/LifeSciences_Gr10",
    "curriculum_docs_auto/Mathematics_Gr7",
    "curriculum_docs_auto/Mathematics_Gr8",
    "curriculum_docs_auto/Mathematics_Gr9",
    "curriculum_docs_auto/Mathematics_Gr10",
    "curriculum_docs_auto/Mathematics_Gr11",
    "curriculum_docs_auto/NaturalSciences_Gr9",
    "curriculum_docs_auto/PhysicalSciences_Gr10",
    "curriculum_docs_auto/PhysicalSciences_Gr11",
    "curriculum_docs_auto/PhysicalSciences_Gr12",
    "curriculum_docs_auto/TechnicalMathematics_Gr10",
    "curriculum_docs_auto/TechnicalMathematics_Gr11",
    "curriculum_docs_auto/TechnicalMathematics_Gr12",
]

for sd in search_dirs:
    if os.path.exists(sd):
        files = glob.glob(f"{sd}/**/*.md", recursive=True)
        print(f"\n=== {sd} ===")
        for f in sorted(files):
            print(f"  {f.replace(os.sep, '/')}")
    else:
        print(f"\n=== {sd} DOES NOT EXIST ===")
