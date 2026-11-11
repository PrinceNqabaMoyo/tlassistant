import glob
import os

print("Files in physical_sciences:")
for f in glob.glob("caps-ai-backend/app/utils/physical_sciences/*.py"):
    print(" ", os.path.basename(f))
