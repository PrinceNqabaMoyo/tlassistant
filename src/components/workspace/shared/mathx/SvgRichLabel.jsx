import React from 'react';

const SUP_MAP = {
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
    '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
    '+': '⁺', '-': '⁻', '=': '⁼', '(': '⁽', ')': '⁾',
    'n': 'ⁿ', 'i': 'ⁱ', 'x': 'ˣ', 'y': 'ʸ'
};

const SUB_MAP = {
    '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
    '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉',
    '+': '₊', '-': '₋', '=': '₌', '(': '₍', ')': '₎',
    'a': 'ₐ', 'e': 'ₑ', 'i': 'ᵢ', 'k': 'ₖ', 'm': 'ₘ',
    'n': 'ₙ', 'o': 'ₒ', 'p': 'ₚ', 'r': 'ᵣ', 's': 'ₛ',
    't': 'ₜ', 'u': 'ᵤ', 'v': 'ᵥ', 'x': 'ₓ'
};

const LATEX_SYMBOL_MAP = [
    [/\^\{\\circ\}|\^\\circ|\\circ/g, '°'],
    [/\{,\}/g, ','],
    [/\\(?:text|mathrm|mathbf|textbf|textit|mathit)\{([^{}]*)\}/g, '$1'],
    [/\\frac\{([^{}]+)\}\{([^{}]+)\}/g, '($1/$2)'],
    [/\\sqrt\{([^{}]+)\}/g, '√($1)'],
    [/\\pi\b/g, 'π'],
    [/\\theta\b/g, 'θ'],
    [/\\alpha\b/g, 'α'],
    [/\\beta\b/g, 'β'],
    [/\\gamma\b/g, 'γ'],
    [/\\Delta\b/g, 'Δ'],
    [/\\delta\b/g, 'δ'],
    [/\\mu\b/g, 'μ'],
    [/\\lambda\b/g, 'λ'],
    [/\\omega\b/g, 'ω'],
    [/\\Omega\b/g, 'Ω'],
    [/\\approx\b/g, '≈'],
    [/\\neq\b/g, '≠'],
    [/\\leq\b|\\le\b/g, '≤'],
    [/\\geq\b|\\ge\b/g, '≥'],
    [/\\times\b/g, '×'],
    [/\\cdot\b/g, '·'],
    [/\\div\b/g, '÷'],
    [/\\pm\b/g, '±'],
    [/\\infty\b/g, '∞'],
    [/\\therefore\b/g, '∴'],
    [/\\parallel\b/g, '∥'],
    [/\\perp\b/g, '⊥'],
    [/\\rightleftharpoons\b/g, '⇌'],
    [/\\rightarrow\b|\\to\b/g, '→'],
    [/\\leftarrow\b/g, '←'],
    [/\\,/g, ' '],
    [/~/g, ' '],
    [/\*\*/g, ''],
    [/\$\$|\$/g, ''],
    [/\\\(|\\\)|\\\[|\\\]/g, '']
];

function toUnicodeSuper(str) {
    const chars = Array.from(String(str));
    if (chars.every((c) => c in SUP_MAP)) {
        return chars.map((c) => SUP_MAP[c]).join('');
    }
    return null;
}

function toUnicodeSub(str) {
    const chars = Array.from(String(str));
    if (chars.every((c) => c in SUB_MAP)) {
        return chars.map((c) => SUB_MAP[c]).join('');
    }
    return null;
}

/**
 * Normalizes a string containing LaTeX/markdown artifacts into clean Unicode text
 * safe for SVG labels, titles, and plain text contexts.
 */
export function cleanSvgText(input) {
    if (input === null || input === undefined) return '';
    let s = String(input);
    for (const [pattern, replacement] of LATEX_SYMBOL_MAP) {
        s = s.replace(pattern, replacement);
    }
    // Convert braced superscripts/subscripts to Unicode where possible
    s = s.replace(/\^\{([^{}]+)\}/g, (_, exp) => toUnicodeSuper(exp) ?? `^(${exp})`);
    s = s.replace(/\^([+-]?\d+|[nxyi])/g, (_, exp) => toUnicodeSuper(exp) ?? `^${exp}`);
    s = s.replace(/_\{([^{}]+)\}/g, (_, sub) => toUnicodeSub(sub) ?? `_${sub}`);
    s = s.replace(/_(\d+|[a-z])/g, (_, sub) => toUnicodeSub(sub) ?? `_${sub}`);
    return s;
}

/**
 * Renders rich SVG label nodes with proper <tspan baselineShift="super|sub">
 * and Unicode symbols so zero raw LaTeX/caret/underscore tokens leak inside <svg><text>.
 * If coordinate/style props (x, y, etc.) are passed, wraps content in <text {...rest}>.
 */
export default function SvgRichLabel({ text, children, ...rest }) {
    const raw = text !== undefined ? text : children;
    if (raw === null || raw === undefined) return null;

    let s = String(raw);
    for (const [pattern, replacement] of LATEX_SYMBOL_MAP) {
        s = s.replace(pattern, replacement);
    }

    const tokenRegex = /(\^\{[^{}]+\}|\^[+-]?\d+|\^[a-zA-Z]|_\{[^{}]+\}|_\d+|_[a-zA-Z])/g;
    const parts = s.split(tokenRegex);
    const rendered = parts.length === 1 ? s : parts.map((part, idx) => {
        if (!part) return null;
        if (part.startsWith('^')) {
            const content = part.startsWith('^{') ? part.slice(2, -1) : part.slice(1);
            const uni = toUnicodeSuper(content);
            return (
                <tspan key={idx} baselineShift="super" fontSize="75%">
                    {uni || content}
                </tspan>
            );
        }
        if (part.startsWith('_')) {
            const content = part.startsWith('_{') ? part.slice(2, -1) : part.slice(1);
            const uni = toUnicodeSub(content);
            return (
                <tspan key={idx} baselineShift="sub" fontSize="75%">
                    {uni || content}
                </tspan>
            );
        }
        return <React.Fragment key={idx}>{part}</React.Fragment>;
    });

    if (rest.x !== undefined || rest.y !== undefined) {
        return <text {...rest}>{rendered}</text>;
    }
    return rendered;
}
