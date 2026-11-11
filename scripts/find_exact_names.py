import glob
import os

print("Files in NaturalSciences_Gr9:")
for f in glob.glob("curriculum_docs_auto/NaturalSciences_Gr9/**/*.md", recursive=True):
    print(" ", f.replace(os.sep, '/'))

print("\nFiles in PhysicalSciences_Gr11/Term 1:")
for f in glob.glob("curriculum_docs_auto/PhysicalSciences_Gr11/Term 1/*.md"):
    print(" ", f.replace(os.sep, '/'))
