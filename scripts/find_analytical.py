import glob

for f in glob.glob("caps-ai-backend/**/*.py", recursive=True):
    if "analytical" in f.lower():
        print(f)
