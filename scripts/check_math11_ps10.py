import os
import glob

dirs = [
    "curriculum_docs_auto/Mathematics_Gr11",
    "curriculum_docs_auto/PhysicalSciences_Gr10"
]
for d in dirs:
    print(f"\n=== {d} ===")
    for f in sorted(glob.glob(f"{d}/**/*.md", recursive=True)):
        print(f"  {f.replace(os.sep, '/')}")
