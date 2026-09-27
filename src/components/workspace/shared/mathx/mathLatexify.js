/**
 * Best-effort conversion of a learner's plain-text maths into LaTeX for a live
 * preview. This is intentionally lightweight — the authoritative parsing happens
 * server-side with SymPy. KaTeX renders with ``throwOnError: false`` so any
 * imperfect output degrades gracefully to the raw text.
 */
export const latexify = (text) => {
    let s = String(text || '');
    if (!s.trim()) return '';

    // Radicals: sqrt(...) / cbrt(...) / root(n, ...)
    s = s.replace(/root\(([^,]+),\s*([^()]*)\)/g, '\\sqrt[$1]{$2}');
    s = s.replace(/sqrt\(([^()]*)\)/g, '\\sqrt{$1}');
    s = s.replace(/cbrt\(([^()]*)\)/g, '\\sqrt[3]{$1}');

    // Exponents: ^{...} already fine; ^number / ^letter -> ^{...}
    s = s.replace(/\^\(([^()]*)\)/g, '^{$1}');
    s = s.replace(/\^(-?\w+)/g, '^{$1}');

    // Subscripts: x_1, T_n, x_(n-1)
    s = s.replace(/_([A-Za-z0-9]+)/g, '_{$1}');
    s = s.replace(/_\(([^()]*)\)/g, '_{$1}');

    // Fractions: (a)/(b) or simple tokens
    s = s.replace(/\(([^()]+)\)\/\(([^()]+)\)/g, '\\frac{$1}{$2}');
    s = s.replace(/([A-Za-z0-9.,]+)\/([A-Za-z0-9.,]+)/g, '\\frac{$1}{$2}');

    // Multiplication / functions / symbols
    s = s.replace(/\*/g, ' \\times ');
    s = s.replace(/\+\-/g, ' \\pm ');
    s = s.replace(/!=/g, ' \\neq ');
    s = s.replace(/<=/g, ' \\leq ');
    s = s.replace(/>=/g, ' \\geq ');
    s = s.replace(/\bapprox\b/g, ' \\approx ');
    s = s.replace(/\bpi\b/g, '\\pi');
    s = s.replace(/\btheta\b/g, '\\theta');
    s = s.replace(/\bdeg\b/g, '^{\\circ}');
    s = s.replace(/\b(sin|cos|tan)\b/g, '\\$1');

    // Decimal comma (SA convention), tight.
    s = s.replace(/(\d),(\d)/g, '$1{,}$2');

    return s;
};
