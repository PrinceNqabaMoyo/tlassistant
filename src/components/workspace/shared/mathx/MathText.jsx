import React from 'react';
import katex from 'katex';
import 'katex/dist/katex.min.css';

/**
 * MathText — renders LaTeX or mixed narrative text with KaTeX.
 *
 * Supports South-African decimal comma convention (e.g. ``0{,}5``),
 * inline delimiters (`\(...\)`, `$...$`), block delimiters (`$$...$$`, `\[...\]`),
 * and formats monetary amounts (Option 1 typography: font-mono).
 * Plain narrative text without math delimiters is rendered as clean text
 * to prevent KaTeX mangling regular words.
 *
 * Props:
 *   latex       the LaTeX source
 *   text        alias for latex prop
 *   display     block (true) vs inline (false) maths
 *   className   extra classes for the wrapper
 */
const DELIMITER_REGEX = /(\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\$[^\$\n]+?\$|\\\([\s\S]*?\\\))/g;
const CURRENCY_REGEX = /(\b(?:R\s*\d{1,3}(?:[ ,]\d{3})*(?:\.\d{2})?|R\s*\d+(?:\.\d{2})?)\b)/g;
const LATEX_COMMAND_REGEX = /\\[a-zA-Z]+|[\^_]\{|\{|\}/;

function renderKatexToString(mathStr, displayMode) {
    try {
        return katex.renderToString(mathStr, {
            throwOnError: false,
            displayMode,
            strict: false,
        });
    } catch {
        return null;
    }
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
                <span key={i} className="font-mono font-semibold text-slate-900">
                    {part}
                </span>
            );
        }
        return part;
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
        return <div className={className}>{renderTextWithCurrency(String(raw))}</div>;
    }

    const rawStr = String(raw);
    const hasDelimiters = DELIMITER_REGEX.test(rawStr);
    DELIMITER_REGEX.lastIndex = 0;

    if (hasDelimiters) {
        const tokens = rawStr.split(DELIMITER_REGEX);
        return (
            <span className={className}>
                {tokens.map((token, index) => {
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
                            return (
                                <span
                                    key={index}
                                    dangerouslySetInnerHTML={{ __html: html }}
                                />
                            );
                        }
                        return <span key={index}>{renderTextWithCurrency(token)}</span>;
                    }

                    return <span key={index}>{renderTextWithCurrency(token)}</span>;
                })}
            </span>
        );
    }

    // No delimiters: check if it's pure LaTeX or plain narrative text
    const looksLikeNarrative = !rawStr.includes('\\') && (rawStr.includes('\n') || rawStr.split(/\s+/).length > 6);
    const hasLatexCommands = LATEX_COMMAND_REGEX.test(rawStr);

    if (!looksLikeNarrative && (hasLatexCommands || (latex && !text))) {
        const html = renderKatexToString(rawStr, false);
        if (html) {
            return (
                <span
                    className={className}
                    dangerouslySetInnerHTML={{ __html: html }}
                />
            );
        }
    }

    // Default clean plain text with currency highlighting
    return <span className={className}>{renderTextWithCurrency(rawStr)}</span>;
};

export default MathText;
