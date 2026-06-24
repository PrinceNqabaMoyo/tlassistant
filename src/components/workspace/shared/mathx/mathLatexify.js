/**
 * Best-effort conversion of a learner's plain-text maths into LaTeX for a live
 * preview. This is intentionally lightweight — the authoritative parsing happens
 * server-side with SymPy. KaTeX renders with ``throwOnError: false`` so any
 * imperfect output degrades gracefully to the raw text.
 */
export const latexify = (text) => {
    let s = String(text || '');
    if (!s.trim()) return '';

    // sqrt(...) / cbrt(...) -> \sqrt{...}
    s = s.replace(/sqrt\(([^()]*)\)/g, '\\sqrt{$1}');
    s = s.replace(/cbrt\(([^()]*)\)/g, '\\sqrt[3]{$1}');

    // Exponents: ^{...} already fine; ^number / ^letter -> ^{...}
    s = s.replace(/\^\(([^()]*)\)/g, '^{$1}');
    s = s.replace(/\^(-?\w+)/g, '^{$1}');

    // Simple fraction a/b (single tokens) -> \frac{a}{b}
    s = s.replace(/([A-Za-z0-9.,]+)\/([A-Za-z0-9.,]+)/g, '\\frac{$1}{$2}');

    // Multiplication / functions
    s = s.replace(/\*/g, ' \\cdot ');
    s = s.replace(/\bpi\b/g, '\\pi');
    s = s.replace(/\btheta\b/g, '\\theta');
    s = s.replace(/\bdeg\b/g, '^{\\circ}');
    s = s.replace(/\b(sin|cos|tan)\b/g, '\\$1');

    // Decimal comma (SA convention), tight.
    s = s.replace(/(\d),(\d)/g, '$1{,}$2');

    return s;
};
