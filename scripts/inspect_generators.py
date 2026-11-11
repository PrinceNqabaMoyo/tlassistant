import os
import glob

print("--- Listing backend generator directories ---")
subdirs = [d for d in glob.glob("caps-ai-backend/app/utils/*") if os.path.isdir(d)]
for d in subdirs:
    py_files = glob.glob(f"{d}/**/*.py", recursive=True)
    print(f"{d} ({len(py_files)} python files)")
