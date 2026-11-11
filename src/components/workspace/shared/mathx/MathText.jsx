import React from 'react';
import katex from 'katex';
import 'katex/dist/katex.min.css';

/**
 * MathText — renders LaTeX, inline exponents/subscripts, chemical formulas,
 * markdown bold, and markdown tables with KaTeX.
 *
 * Guarantees zero raw LaTeX/markdown leaks (^, _, {,}, **, \frac, \text, pipe tables)
 * in both Student Workspace and Super Admin Vetting Workbench.
 */
const DELIMITER_REGEX = /(\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\$[^\$\n]+?\$|\\\([\s\S]*?\\\))/g;
const CURRENCY_REGEX = /(\bR\s*\d{1,3}(?:[ ]\d{3})*(?:[.,]\d{1,2})?|\bR\s*\d+(?:[.,]\d{1,2})?)/g;
const LATEX_COMMAND_REGEX = /\\[a-zA-Z]+|[\^_]\{|\{|\}/;

const INLINE_SYMBOL_REPLACEMENTS = [
    [/\^\{\\circ\}|\^\\circ|\\circ\b|\\circ/g, '°'],
    [/\{,\}/g, ','],
    [/\\(?:text|mathrm|mathbf|textbf)\{([^{}]*)\}/g, '$1'],
    [/\\therefore\b/g, '∴'],
    [/\\because\b/g, '∵'],
    [/\\approx\b/g, '≈'],
    [/\\neq\b/g, '≠'],
    [/\\leq\b|\\le\b/g, '≤'],
    [/\\geq\b|\\ge\b/g, '≥'],
    [/\\times\b/g, '×'],
    [/\\cdot\b/g, '·'],
    [/\\div\b/g, '÷'],
    [/\\pm\b/g, '±'],
    [/\\infty\b/g, '∞'],
    [/\\pi\b/g, 'π'],
    [/\\theta\b/g, 'θ'],
    [/\\alpha\b/g, 'α'],
    [/\\beta\b/g, 'β'],
    [/\\gamma\b/g, 'γ'],
    [/\\Delta\b/g, 'Δ'],
    [/\\mu\b/g, 'μ'],
    [/\\lambda\b/g, 'λ'],
    [/\\Omega\b/g, 'Ω'],
    [/\\angle\b/g, '∠'],
    [/\\triangle\b/g, '△'],
    [/\\perp\b/g, '⊥'],
    [/\\parallel\b/g, '∥'],
    [/\\rightleftharpoons\b/g, '⇌'],
    [/\\rightarrow\b|\\to\b/g, '→'],
    [/\\leftarrow\b/g, '←'],
    [/\bSS\[(M|A|CA)\]/g, '[$1]'],
    [/~/g, ' ']
];

// Matches undelimited LaTeX fractions/roots or tokens with ^ / _ (exponents, units, chemical formulas, subscripts)
const UNDELIMITED_MATH_TOKEN_REGEX = /(\\(?:frac\{[^{}]+\}\{[^{}]+\}|sqrt\{[^{}]+\})|[A-Za-z0-9)\]}]+(?:[\^_](?:\{[^{}]+\}|[+-]?\d+[+-]?|[a-zA-Z]))+)/g;

function renderKatexToString(mathStr, displayMode) {
    try {
        let normalized = String(mathStr).replace(/\{,\}/g, ',');
        // Normalize LaTeX array alignments that KaTeX does not support (e.g. {r@{,}l} or {r@,l}) to {crl}
        normalized = normalized.replace(/\{array\}\{[^}]*@[^}]*\}/g, '{array}{crl}');
        return katex.renderToString(normalized, {
            throwOnError: false,
            displayMode,
            strict: false,
        });
    } catch {
        return null;
    }
}

function renderSupSubToken(token, key) {
    if (token.startsWith('\\frac') || token.startsWith('\\sqrt')) {
        const html = renderKatexToString(token, false);
        if (html) {
            return <span key={key} dangerouslySetInnerHTML={{ __html: html }} />;
        }
    }
    // Parse base and sequence of ^... and _... segments into semantic <sup> and <sub>
    const parts = token.split(/([\^_](?:\{[^{}]+\}|[+-]?\d+[+-]?|[a-zA-Z]))/g);
    return (
        <span key={key} className="whitespace-nowrap">
            {parts.map((p, idx) => {
                if (!p) return null;
                if (p.startsWith('^')) {
                    const val = p.startsWith('^{') ? p.slice(2, -1) : p.slice(1);
                    return <sup key={idx} className="text-[0.75em] leading-none font-medium">{val}</sup>;
                }
                if (p.startsWith('_')) {
                    const val = p.startsWith('_{') ? p.slice(2, -1) : p.slice(1);
                    return <sub key={idx} className="text-[0.75em] leading-none font-medium">{val}</sub>;
                }
                return <React.Fragment key={idx}>{p}</React.Fragment>;
            })}
        </span>
    );
}

function renderTextWithCurrency(text) {
    if (!text || typeof text !== 'string') return text;
    if (!text.includes('R')) return text;
    const parts = text.split(CURRENCY_REGEX);
    if (parts.length === 1) return text;
    return parts.map((part, i) => {
        if (CURRENCY_REGEX.test(part)) {
            CURRENCY_REGEX.lastIndex = 0;
            return (
                <span key={i} className="font-semibold text-slate-900 whitespace-nowrap">
                    {part}
                </span>
            );
        }
        return part;
    });
}

function renderPlainSegmentWithSupSub(segment, keyPrefix = 'seg') {
    if (!segment) return null;
    let cleaned = String(segment);
    for (const [rx, rep] of INLINE_SYMBOL_REPLACEMENTS) {
        cleaned = cleaned.replace(rx, rep);
    }

    const subTokens = cleaned.split(UNDELIMITED_MATH_TOKEN_REGEX);
    if (subTokens.length === 1) {
        return renderTextWithCurrency(cleaned);
    }

    return subTokens.map((sub, idx) => {
        if (!sub) return null;
        UNDELIMITED_MATH_TOKEN_REGEX.lastIndex = 0;
        if (UNDELIMITED_MATH_TOKEN_REGEX.test(sub)) {
            UNDELIMITED_MATH_TOKEN_REGEX.lastIndex = 0;
            return renderSupSubToken(sub, `${keyPrefix}-m-${idx}`);
        }
        return <React.Fragment key={`${keyPrefix}-t-${idx}`}>{renderTextWithCurrency(sub)}</React.Fragment>;
    });
}

function renderSegmentWithBoldAndSupSub(segment, keyPrefix = 'bseg') {
    if (!segment) return null;
    const str = String(segment);
    if (!str.includes('**')) {
        return renderPlainSegmentWithSupSub(str, keyPrefix);
    }
    const boldParts = str.split(/(\*\*[^*]+\*\*)/g);
    return boldParts.map((bp, i) => {
        if (!bp) return null;
        if (bp.startsWith('**') && bp.endsWith('**') && bp.length > 4) {
            return (
                <strong key={`${keyPrefix}-b-${i}`} className="font-semibold text-slate-900">
                    {renderPlainSegmentWithSupSub(bp.slice(2, -2), `${keyPrefix}-bi-${i}`)}
                </strong>
            );
        }
        return <React.Fragment key={`${keyPrefix}-p-${i}`}>{renderPlainSegmentWithSupSub(bp, `${keyPrefix}-pi-${i}`)}</React.Fragment>;
    });
}

function unwrapTextCommands(str) {
    if (!str || typeof str !== 'string') return str;
    let s = str;
    const target = '\\text{';
    while (s.includes(target)) {
        const start = s.indexOf(target);
        let depth = 1;
        let pos = start + target.length;
        while (pos < s.length && depth > 0) {
            if (s[pos] === '{' && (pos === 0 || s[pos - 1] !== '\\')) {
                depth++;
            } else if (s[pos] === '}' && (pos === 0 || s[pos - 1] !== '\\')) {
                depth--;
            }
            pos++;
        }
        if (depth === 0) {
            const inner = s.slice(start + target.length, pos - 1);
            s = s.slice(0, start) + inner + s.slice(pos);
        } else {
            s = s.slice(0, start) + s.slice(start + target.length);
        }
    }
    return s;
}

function renderTallyMarksSvg(count, keyPrefix = 'tly') {
    const n = Math.min(Math.max(0, Number(count) || 0), 100);
    if (n === 0) return <span className="font-mono text-slate-400">0</span>;
    const fullGroups = Math.floor(n / 5);
    const remainder = n % 5;
    const groups = [];
    for (let g = 0; g < fullGroups; g++) {
        groups.push(
            <svg key={`${keyPrefix}-g-${g}`} width="22" height="16" viewBox="0 0 22 16" className="inline-block mx-0.5 align-middle text-slate-800">
                <line x1="3" y1="2" x2="3" y2="14" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />
                <line x1="7.5" y1="2" x2="7.5" y2="14" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />
                <line x1="12" y1="2" x2="12" y2="14" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />
                <line x1="16.5" y1="2" x2="16.5" y2="14" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />
                <line x1="1" y1="13" x2="19" y2="3" stroke="#13519C" strokeWidth="2" strokeLinecap="round" />
            </svg>
        );
    }
    if (remainder > 0) {
        groups.push(
            <svg key={`${keyPrefix}-rem`} width={remainder * 4.5 + 4} height="16" viewBox={`0 0 ${remainder * 4.5 + 4} 16`} className="inline-block mx-0.5 align-middle text-slate-800">
                {Array.from({ length: remainder }).map((_, idx) => (
                    <line
                        key={idx}
                        x1={3 + idx * 4.5}
                        y1="2"
                        x2={3 + idx * 4.5}
                        y2="14"
                        stroke="currentColor"
                        strokeWidth="1.8"
                        strokeLinecap="round"
                    />
                ))}
            </svg>
        );
    }
    return <span className="inline-flex items-center flex-wrap gap-0.5">{groups}</span>;
}

function renderInlineMathAndText(rawStr, keyPrefix = 'inl') {
    if (!rawStr) return null;
    let preprocessed = String(rawStr)
        .replace(/\\r\\n/g, '\n')
        .replace(/\\n/g, '\n');
    if (preprocessed.includes('\\text{')) {
        preprocessed = unwrapTextCommands(preprocessed);
    }
    const tallyMatch = preprocessed.trim().match(/^\[TALLY:(\d+)\]$/i);
    if (tallyMatch) {
        return renderTallyMarksSvg(parseInt(tallyMatch[1], 10), keyPrefix);
    }
    // Normalize bold-wrapped inline math (**$...$** or **\(...\)**) so ** never splits across tokens
    const normalizedStr = preprocessed.replace(/\*\*(\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\$[^\$\n]+?\$|\\\([\s\S]*?\\\))\*\*/g, '$1');
    const hasDelimiters = DELIMITER_REGEX.test(normalizedStr);
    DELIMITER_REGEX.lastIndex = 0;

    if (hasDelimiters) {
        const tokens = normalizedStr.split(DELIMITER_REGEX);
        return tokens.map((token, index) => {
            if (!token) return null;
            let mathContent = null;
            let isBlock = false;

            if (token.startsWith('$$') && token.endsWith('$$') && token.length >= 4) {
                mathContent = token.slice(2, -2);
                isBlock = true;
            } else if (token.startsWith('\\[') && token.endsWith('\\]') && token.length >= 4) {
                mathContent = token.slice(2, -2);
                isBlock = true;
            } else if (token.startsWith('\\(') && token.endsWith('\\)') && token.length >= 4) {
                mathContent = token.slice(2, -2);
                isBlock = false;
            } else if (token.startsWith('$') && token.endsWith('$') && token.length >= 2) {
                mathContent = token.slice(1, -1);
                isBlock = false;
            }

            if (mathContent !== null) {
                const html = renderKatexToString(mathContent, isBlock);
                if (html) {
                    return <span key={`${keyPrefix}-${index}`} dangerouslySetInnerHTML={{ __html: html }} />;
                }
                return <span key={`${keyPrefix}-${index}`}>{renderSegmentWithBoldAndSupSub(mathContent, `${keyPrefix}-${index}`)}</span>;
            }

            return <span key={`${keyPrefix}-${index}`}>{renderSegmentWithBoldAndSupSub(token.replace(/\*\*/g, ''), `${keyPrefix}-${index}`)}</span>;
        });
    }

    // Check if the string contains English prose words (3+ consecutive letters that are not a LaTeX command)
    const strippedCommands = preprocessed.replace(/\\[a-zA-Z]+/g, '');
    const englishWordCount = (strippedCommands.match(/\b[a-zA-Z]{3,}\b/g) || []).length;
    const looksLikeNarrative = preprocessed.includes('\n') || preprocessed.split(/\s+/).length > 4 || englishWordCount >= 2;
    const hasLatexCommands = LATEX_COMMAND_REGEX.test(preprocessed);

    if (!looksLikeNarrative && hasLatexCommands && !preprocessed.includes('**')) {
        const html = renderKatexToString(preprocessed, false);
        if (html) {
            return <span dangerouslySetInnerHTML={{ __html: html }} />;
        }
    }

    return renderSegmentWithBoldAndSupSub(preprocessed, keyPrefix);
}

function isTableSeparatorLine(line) {
    const t = line.trim();
    return t.startsWith('|') && t.endsWith('|') && /^\|[\s:|-]+\|$/.test(t) && t.includes('-');
}

function parseRowCells(line) {
    return line
        .trim()
        .replace(/^\|/, '')
        .replace(/\|$/, '')
        .split('|')
        .map((c) => c.trim());
}

/**
 * Splits multi-line text into narrative blocks and Markdown tables so pipe tables
 * render as semantic HTML <table> elements.
 */
function renderBlocksWithTables(rawStr) {
    const lines = rawStr.split('\n');
    const blocks = [];
    let i = 0;

    while (i < lines.length) {
        if (
            i + 1 < lines.length &&
            lines[i].trim().startsWith('|') &&
            lines[i].trim().endsWith('|') &&
            isTableSeparatorLine(lines[i + 1])
        ) {
            const headerCells = parseRowCells(lines[i]);
            i += 2;
            const bodyRows = [];
            while (i < lines.length && lines[i].trim().startsWith('|') && lines[i].trim().endsWith('|')) {
                if (!isTableSeparatorLine(lines[i])) {
                    bodyRows.push(parseRowCells(lines[i]));
                }
                i++;
            }
            blocks.push({ type: 'table', headerCells, bodyRows });
        } else {
            const textLines = [];
            while (
                i < lines.length &&
                !(
                    i + 1 < lines.length &&
                    lines[i].trim().startsWith('|') &&
                    lines[i].trim().endsWith('|') &&
                    isTableSeparatorLine(lines[i + 1])
                )
            ) {
                textLines.push(lines[i]);
                i++;
            }
            blocks.push({ type: 'text', content: textLines.join('\n') });
        }
    }

    return blocks.map((b, bIdx) => {
        if (b.type === 'table') {
            const isTallyCol = b.headerCells.map((h) => /\btall(?:y|ies)\b/i.test(String(h)));
            return (
                <div key={`tbl-${bIdx}`} className="my-2 overflow-x-auto rounded-lg border border-slate-200">
                    <table className="min-w-full divide-y divide-slate-200 text-xs">
                        <thead className="bg-slate-50">
                            <tr>
                                {b.headerCells.map((hc, cIdx) => (
                                    <th key={cIdx} className="px-3 py-1.5 text-center font-semibold text-slate-700 border-r last:border-r-0 border-slate-200">
                                        {renderInlineMathAndText(hc, `th-${bIdx}-${cIdx}`)}
                                    </th>
                                ))}
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-slate-100 bg-white">
                            {b.bodyRows.map((row, rIdx) => (
                                <tr key={rIdx}>
                                    {row.map((cell, cIdx) => {
                                        const trimmedCell = String(cell || '').trim();
                                        const isTallyNumber = isTallyCol[cIdx] && /^\d+$/.test(trimmedCell);
                                        return (
                                            <td key={cIdx} className="px-3 py-1.5 text-center font-mono text-slate-800 border-r last:border-r-0 border-slate-100">
                                                {isTallyNumber
                                                    ? renderTallyMarksSvg(parseInt(trimmedCell, 10), `tly-${bIdx}-${rIdx}-${cIdx}`)
                                                    : renderInlineMathAndText(cell, `td-${bIdx}-${rIdx}-${cIdx}`)}
                                            </td>
                                        );
                                    })}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            );
        }
        return <React.Fragment key={`txt-${bIdx}`}>{renderInlineMathAndText(b.content, `blk-${bIdx}`)}</React.Fragment>;
    });
}

const MathText = ({ latex = '', text = '', display = false, className = '' }) => {
    const raw = latex || text || '';

    if (!raw) return null;

    if (display) {
        const html = renderKatexToString(String(raw), true);
        if (html) {
            return <div className={className} dangerouslySetInnerHTML={{ __html: html }} />;
        }
        return <div className={className}>{renderSegmentWithBoldAndSupSub(String(raw), 'disp')}</div>;
    }

    const rawStr = String(raw)
        .replace(/\\r\\n/g, '\n')
        .replace(/\\n/g, '\n');
    if (rawStr.includes('|') && rawStr.includes('\n')) {
        return <span className={className}>{renderBlocksWithTables(rawStr)}</span>;
    }

    return <span className={className}>{renderInlineMathAndText(rawStr, 'root')}</span>;
};

export default MathText;
