"""Shared text hygiene for scraped curriculum markdown.

Both harvesters (bs_docs_harvester, sci_docs_harvester) read the SAME
pymupdf4llm-produced markdown, and that markdown carries three artefact classes
into learner-facing fields:

1. LaTeX maths. 'Physical Sciences' alone holds ~44k escapes, and auditing every
   string of every harvested science item found leaked memos reading
   'Forward force (F_{ {applied}}) = 600 { N}'.
2. Markdown-escaped punctuation. Business Studies output contained
   '1\\. Moral characteristics...' and 'DIAGRAM\\[A radial...' and '\\[6]' for a
   6-mark allocation - 145 of 4,822 harvested BS units.
3. Inline HTML from the textbook's highlight/superscript formatting:
   '## **<mark>Water purification</mark>**, 'NH<sub>4</sub><sup>+</sup>'.
   <mark> in a heading also broke syllabus-topic matching outright.

Science questions are plain-text and tabular fields with no KaTeX renderer, and
so are Business Studies rubrics, so the markup must be RESOLVED, not deleted:
'{ N}' has to keep its unit, '\\times 100' has to keep its '× 100' and '\\[6]' has
to keep its brackets. Applied at document-load time in each harvester, so the
grounding audit and the item text always see the identical string.

Pure string functions: no file access, no LLM, no network.
"""
from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# LaTeX de-escaping
# ---------------------------------------------------------------------------
MATH_SYMBOLS = {
    "\\times": "\u00d7", "\\cdot": "\u00b7", "\\div": "\u00f7", "\\pm": "\u00b1",
    "\\mp": "\u2213", "\\approx": "\u2248", "\\leq": "\u2264", "\\geq": "\u2265",
    "\\neq": "\u2260", "\\equiv": "\u2261", "\\propto": "\u221d", "\\degree": "\u00b0",
    "\\rightarrow": "\u2192", "\\leftarrow": "\u2190", "\\to": "\u2192",
    "\\alpha": "\u03b1", "\\beta": "\u03b2", "\\gamma": "\u03b3", "\\delta": "\u03b4",
    "\\Delta": "\u0394", "\\theta": "\u03b8", "\\lambda": "\u03bb", "\\mu": "\u03bc",
    "\\nu": "\u03bd", "\\rho": "\u03c1", "\\sigma": "\u03c3", "\\tau": "\u03c4",
    "\\phi": "\u03c6", "\\omega": "\u03c9", "\\Omega": "\u03a9", "\\pi": "\u03c0",
    "\\sum": "\u03a3", "\\infty": "\u221e", "\\sinh": "sinh", "\\cosh": "cosh",
    "\\tan": "tan", "\\sin": "sin", "\\cos": "cos", "\\log": "log", "\\ln": "ln",
}
SYM_RE = re.compile(
    "|".join(re.escape(k) + r"(?![A-Za-z])" for k in
             sorted(MATH_SYMBOLS, key=len, reverse=True)))
SUPERSCRIPT = {"-": "\u207b", "+": "\u207a", "0": "\u2070", "1": "\u00b9",
               "2": "\u00b2", "3": "\u00b3", "4": "\u2074", "5": "\u2075",
               "6": "\u2076", "7": "\u2077", "8": "\u2078", "9": "\u2079",
               "n": "\u207f", "x": "\u02e3", "m": "\u1d50", "N": "\u0274"}
SUBSCRIPT = {"0": "\u2080", "1": "\u2081", "2": "\u2082", "3": "\u2083",
             "4": "\u2084", "5": "\u2085", "6": "\u2086", "7": "\u2087",
             "8": "\u2088", "9": "\u2089"}

# anything that looks like maths markup. Bare '{ N}' unit braces and bare
# 'H_2SO_4' subscripts count too: the leaked memo 'Initial velocity (v_i) = 20
# { m} {s}-1' has no backslash at all, so a guard on \ $ only would have passed
# it straight through. '^+'/'^-' count as well, because an HTML ion charge
# ('<sup>+</sup>') arrives here as a sign with no digit after it. Every other
# pass in delatex needs a backslash, a $ or a brace, so widening the guard
# cannot alter ordinary prose.
LATEXISH = re.compile(r"\\|\$|[_^]\{|\{[^{}]*\}|_\d|\^\d|\^[+-]")

# pymupdf4llm keeps the textbook's highlight/underline/superscript formatting as
# inline HTML: '## **<mark>Water purification</mark>**'. A heading cleaner that
# strips the '**' but not the tags yields 'mark>Water purification</mark', which
# matches no syllabus topic, and the same tags leak into question prompts.
# Contents are kept (superscripts carry meaning), the tags are not.
INLINE_TAG_RE = re.compile(
    r"</?(?:mark|u|sup|sub|span|div|b|i|em|strong)\s*/?>", re.I)
SUP_TAG_RE = re.compile(r"<sup(?:\s[^>]*)?>(.+?)</sup>", re.I | re.S)
SUB_TAG_RE = re.compile(r"<sub(?:\s[^>]*)?>(.+?)</sub>", re.I | re.S)


def html_to_text(text: str) -> str:
    """'<sup>+</sup>' -> '^+', '<sub>2</sub>' -> '_2', other inline tags dropped.

    The corpus is full of these: an audited Physical Sciences memo read
    'NH3(g) + H<sup>+</sup> (aq) -> NH<sup>+</sup> 4<sup>(aq)</sup>'. Converting
    the tags into script notation BEFORE delatex means one pass renders the
    unicode (H\u207a), instead of leaving raw HTML in a learner-facing field.
    """
    text = SUP_TAG_RE.sub(lambda m: "^" + m.group(1).strip(), text)
    text = SUB_TAG_RE.sub(lambda m: "_" + m.group(1).strip(), text)
    return INLINE_TAG_RE.sub("", text)


def delatex(text: str) -> str:
    """Resolve LaTeX/markdown maths escapes into readable plain text."""
    if not LATEXISH.search(text):
        return text                      # the overwhelming majority of chapters
    out = re.sub(r"\$\$(.+?)\$\$", r" \1 ", text, flags=re.S)
    out = re.sub(r"\$(.+?)\$", r" \1 ", out, flags=re.S)
    # A delimiter becomes a space only when it CLOSES: '\[ \sum x \]' is display
    # maths. An unpaired '\[' is markdown-escaped punctuation - '\[6]' is a
    # 6-mark allocation - and deleting only its opener left '6]'.
    out = re.sub(r"\\\[(.+?)\\\]", r" \1 ", out, flags=re.S)
    out = re.sub(r"\\\((.+?)\\\)", r" \1 ", out, flags=re.S)
    out = out.replace("\\[", "[").replace("\\]", "]")
    out = out.replace("\\(", "(").replace("\\)", ")")
    # \text{...} and \frac{...}{...} nest each other in both directions
    # (\frac{\text{Total Cost}}{\text{Total Units}}, \frac{F_{s(max)}}{N}), so a
    # single pass cannot work: allow ONE level of inner braces in the arguments
    # and repeat to a fixed point, which resolves deeper nesting inside-out.
    arg = r"(?:[^{}]|\{[^{}]*\})*"
    for _ in range(6):
        prev = out
        out = re.sub(r"\\(?:text|textrm|textbf|textit|mathrm|mathit|mathbf|mathsf"
                     r"|operatorname|boxed|underbrace|overbrace)\s*\{(" + arg + r")\}",
                     r"\1", out)
        out = re.sub(r"\\(?:d|t)?frac\s*\{(" + arg + r")\}\s*\{(" + arg + r")\}",
                     r"(\1)/(\2)", out)
        out = re.sub(r"\\sqrt\s*\{(" + arg + r")\}", "\u221a(\\1)", out)
        if out == prev:
            break
    out = re.sub(r"\\(?:left|right|displaystyle|textstyle|quad|qquad|limits)"
                 r"|\\[,;:! ]", " ", out)
    out = SYM_RE.sub(lambda m: MATH_SYMBOLS[m.group(0)], out)
    out = re.sub(r"\\([%_#*&$'\"])", r"\1", out)           # markdown-escaped chars
    out = re.sub(r"\^\\circ", "\u00b0", out)
    for _ in range(5):                   # unwrap braces, innermost first
        new = re.sub(r"\{\s*([^{}]*?)\s*\}", r"\1", out)
        if new == out:
            break
        out = new

    def _sup(m):
        # x^2, 10^-3, t^n, and ion charges H^+ / Cu^2+; leave anything unmapped
        # exactly as written rather than inventing characters (an early version
        # produced '^^y'), and never consume a lone '^' with nothing after it.
        chars = m.group(1)
        if not chars:
            return m.group(0)
        return "".join(SUPERSCRIPT[c] for c in chars) if all(
            c in SUPERSCRIPT for c in chars) else m.group(0)

    # The sign must be able to stand ALONE: 'H^+' has no digit, so requiring one
    # after [+-]? left every converted '<sup>+</sup>' charge as literal '^+'.
    out = re.sub(r"\^\{?([+-]?[\dn]{0,4}[+-]?)\}?", _sup, out)
    # subscript WITHOUT keeping the underscore: H_{2}O must read 'H\u2082O', the way a
    # textbook prints it, not 'H_\u2082O'
    out = re.sub(r"_(\d{1,3})",
                 lambda m: "".join(SUBSCRIPT.get(c, c) for c in m.group(1)), out)
    out = out.replace("{", "").replace("}", "")
    out = re.sub(r"\\(?![A-Za-z0-9])", "", out)  # leftover escape punctuation
    return re.sub(r"[ 	]{2,}", " ", out)


def prepare_text(text: str) -> str:
    """Full document hygiene for a scraped chapter, in dependency order.

    html_to_text first, so its '^'/'_' output is rendered by delatex in the same
    pass instead of surviving as markup.
    """
    return delatex(html_to_text(text))
