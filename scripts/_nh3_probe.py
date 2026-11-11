"""Exact divergence for the one ungrounded PS Gr12 memo: same code path as
_sci_verify.py (norm over _load_all texts), plus a longest-common-prefix search
so the first differing character is visible.
"""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps-ai-backend"))
from app.utils import sci_docs_harvester as S

# write our own UTF-8 report: PowerShell's '>' re-encodes stdout and mojibake's
# every '->' and '^+' in the console
sys.stdout = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
               "_out_nh3.txt"), "w", encoding="utf-8")

KEY = "grade12_physical_sciences_acids_bases"


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", S._clean(s).lower())


g = S._grade_of(None, KEY)
texts, sidecar, paths, rejected = S._load_all(g, KEY)
src = norm(" ".join(texts))
print("paths=", [os.path.basename(p) for p in paths])
print("sidecar=", bool(sidecar), "sidecar_len=", len(sidecar or ""))
print("src_norm_len=", len(src))

for i in S.harvest_items(None, KEY):
    if i.get("kind") == "mcq":
        continue
    for m in i.get("marking_points") or []:
        n = norm(m)
        if len(n) < 25 or n in src:
            continue
        print("\nUNGROUNDED mp:", repr(m))
        print("  norm:", repr(n))
        # longest prefix of n that IS in src, then what follows in both
        lo, hi = 0, len(n)
        while hi > 0 and n[:hi] not in src:
            hi -= 1
        pos = src.find(n[:hi]) if hi else 0
        print(f"  common prefix len={hi} -> {n[:hi]!r}")
        print(f"  memo continues : {n[hi:hi + 40]!r}")
        print(f"  source continues: {src[pos + hi:pos + hi + 40]!r}")

# where did the adjacency go? compare raw vs normalized around the sentence
raw = " ".join(texts)
for probe in ("NH3 accepts a proton", "accepts a proton. It is a"):
    print(f"\nraw contains {probe!r}: {probe in raw}")
print("src contains 'nh3accepts':", "nh3accepts" in src)
print("src contains 'acceptsaproton':", "acceptsaproton" in src)
k = raw.find("NH3 accepts a proton")
if k < 0:
    k = raw.find("accepts a proton")
print("\nRAW window :", repr(raw[k - 40:k + 140]))
print("NORM window:", repr(norm(raw[k - 40:k + 140])))
print("\n_clean only on that window:", repr(S._clean(raw[k - 40:k + 140])))
