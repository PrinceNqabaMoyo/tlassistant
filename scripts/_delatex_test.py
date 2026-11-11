"""Unit tests for _delatex: real leaked strings + things it must not break.

Writes its own UTF-8 report (console is cp1252 and mangles ₂/θ/×).
"""
import sys, os, re, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps-ai-backend"))
from app.utils.sci_docs_harvester import _delatex, _prepare  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_out_delatex.txt")

CASES = [
    # the 6 real learner-facing leaks found by the audit
    ("Forward force (F_{ {applied}}) = 600 { N}",
     "Forward force (F_applied) = 600 N"),
    ("Resultant Force (F_{ {net}})", "Resultant Force (F_net)"),
    ("Total mass (m_{ {total}}) = 1200 { kg} + 1200 { kg} = 2400 { kg}",
     "Total mass (m_total) = 1200 kg + 1200 kg = 2400 kg"),
    ("Initial velocity (v_i) = 20 { m} {s}-1", "Initial velocity (v_i) = 20 m s-1"),
    # maths shapes that actually occur in the corpus
    ("$\\text{Weighted Average Cost} = \\frac{\\text{Total Cost}}{\\text{Total Units}}$",
     "Weighted Average Cost = (Total Cost)/(Total Units)"),
    ("\\( \\sin { \\theta } \\)", "sin θ"),
    ("H_{2}O and CO_{2}", "H₂O and CO₂"),
    ("a = 9{,}8 m s^{-2}", "a = 9,8 m s⁻²"),
    ("50 \\% of the energy", "50 % of the energy"),
    ("E = mc^{2}", "E = mc²"),
    ("v \\times t", "v × t"),
    ("25 \\degree C", "25 ° C"),
    ("$$\\frac{Gross\\ Profit}{Sales} \\times 100$$", "(Gross Profit)/(Sales) × 100"),
    ("$\\frac{R\\_x}{R}$", "(R_x)/(R)"),
    ("\\frac{F_{s(max)}}{N}", "(F_s(max))/(N)"),
    ("F_f = \\mu N", "F_f = μ N"),
    ("W = \\Delta E_p", "W = Δ E_p"),
    ("n(H_2SO_4)", "n(H₂SO₄)"),
    ("10^{-3} dm^3", "10⁻³ dm³"),
    # ion charges: a sign with no digit, and a digit then a sign. Both the
    # superscript pass and the fast-path guard have to cope, or the '<sup>+</sup>'
    # that _html_to_text produces stays literal in front of the learner.
    ("H^+ ions", "H⁺ ions"),
    ("Cu^2+ and SO_4^2-", "Cu²⁺ and SO₄²⁻"),
    # the Business Studies leaks, taken from the corpus as they really appear:
    # an escaped mark allocation and an escaped bracketed diagram note. Neither
    # closes with '\]', so both must keep their brackets.
    ("1\\. Moral characteristics that define an organisation. \\[6]",
     "1. Moral characteristics that define an organisation. [6]"),
    ("DIAGRAM\\[Smart art Radial showing General management at the centre ]",
     "DIAGRAM[Smart art Radial showing General management at the centre ]"),
    # a PAIRED '\[ ... \]' is LaTeX display maths, and there the delimiters are
    # the noise and must go
    ("\\[ \\sum x \\]", "Σ x"),
    # must survive untouched
    ("The nucleus contains protons and neutrons.",
     "The nucleus contains protons and neutrons."),
    ("Osmosis is the movement of water from a dilute solution.",
     "Osmosis is the movement of water from a dilute solution."),
]

lines, fails = [], 0
for src, want in CASES:
    got = _delatex(src).strip()
    ok = got == want.strip()
    fails += 0 if ok else 1
    lines.append(f"{'ok  ' if ok else 'FAIL'}  {src!r}\n        got={got!r}")
    if not ok:
        lines.append(f"        want={want!r}")

# HTML script tags reach the harvester through _prepare, not _delatex
PREPARE_CASES = [
    ("NH3(g) + H<sup>+</sup> (aq) \u2192 NH<sub>4</sub><sup>+</sup>(aq)",
     "NH3(g) + H⁺ (aq) → NH₄⁺(aq)"),
    ("## <mark>Water purification</mark>", "## Water purification"),
    ("O<sub>2</sub> and CO<sub>2</sub>", "O₂ and CO₂"),
    ("<u>photosynthesis</u> is endothermic", "photosynthesis is endothermic"),
    ("H<sup>+</sup> and OH<sup>-</sup> make water", "H⁺ and OH⁻ make water"),
]
for src, want in PREPARE_CASES:
    got = _prepare(src).strip()
    ok = got == want.strip()
    fails += 0 if ok else 1
    lines.append(f"{'ok  ' if ok else 'FAIL'}  [_prepare] {src!r}\n        got={got!r}")
    if not ok:
        lines.append(f"        want={want!r}")

# stability, residue and speed on the heaviest real chapter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
worst = None
for dp, _d, fns in os.walk(os.path.join(ROOT, "curriculum_docs_auto")):
    if os.path.basename(dp) == "images":
        continue
    for fn in fns:
        if fn.endswith(".md"):
            p = os.path.join(dp, fn)
            n = os.path.getsize(p)
            if worst is None or n > worst[1]:
                worst = (p, n)
raw = open(worst[0], encoding="utf-8", errors="replace").read()
t0 = time.time()
once = _delatex(raw)
ms = (time.time() - t0) * 1000
twice = _delatex(once)
residue = re.findall(r"\\frac|\\text\{|\\left|\\right|\\times|\$\$|\\\("
                     r"|_\{|\^\{|<sup|<sub|<mark", twice)
html_left = re.findall(r"<(?:sup|sub|mark|u)>|</(?:sup|sub|mark|u)>", _prepare(raw))
lines.append(f"\n{os.path.relpath(worst[0], ROOT)} chars={len(raw)} in {ms:.0f} ms")
lines.append(f"  idempotent={once == twice}  residue_latex_after_2_passes={len(residue)}")
lines.append(f"  html tags left after _prepare={len(html_left)}")
lines.append(f"  size {len(raw)} -> {len(once)} (delta {len(once) - len(raw)})")
for m in list(re.finditer(r"\\[A-Za-z]+", twice))[:8]:
    lines.append("   leftover cmd: " + twice[m.start():m.start() + 60].replace("\n", " "))

lines.append(f"\n{len(CASES) + len(PREPARE_CASES) - fails}/{len(CASES) + len(PREPARE_CASES)} cases pass")
open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print(f"{len(CASES) + len(PREPARE_CASES) - fails}/{len(CASES) + len(PREPARE_CASES)} pass "
      f"-> see {os.path.basename(OUT)}")
sys.exit(1 if fails else 0)
