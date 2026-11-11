import glob
import re
import os
from collections import defaultdict

pattern = os.path.join("playwright-test", "Gr*", "*", "*.md")
missing_by_track = defaultdict(lambda: [0, 0])

for p in glob.glob(pattern):
    parts = p.split(os.sep)
    track = f"{parts[-3]} {parts[-2]}"
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()
    steps = re.split(r"### Step \d+:", c)[1:]
    for st in steps:
        if "**Official Worked Solution:**" in st:
            missing_by_track[track][0] += 1
        else:
            missing_by_track[track][1] += 1

print(f"{'Track':35} | {'Has Sol':8} | {'Missing Sol':11} | {'Missing Pct':11}")
print("-" * 72)
for tr, (has_s, miss_s) in sorted(missing_by_track.items(), key=lambda x: -x[1][1]):
    total = has_s + miss_s
    pct = round(miss_s / total * 100, 1)
    if miss_s > 0:
        print(f"{tr:35} | {has_s:8} | {miss_s:11} | {pct:10}%")
