import React from 'react';

const readBalancedParen = (s, startIdx) => {
    let depth = 0;
    let i = startIdx;
    if (s[i] !== '(') return null;
    depth = 1;
    i += 1;
    const contentStart = i;
    while (i < s.length) {
        const ch = s[i];
        if (ch === '(') depth += 1;
        if (ch === ')') depth -= 1;
        if (depth === 0) {
            return {
                content: s.slice(contentStart, i),
                endIdx: i,
            };
        }
        i += 1;
    }
    return null;
};

export const renderMathText = (input) => {
    const text = String(input ?? '').replace(/\*/g, '×');
    if (!text.includes('^')) return text;

    const out = [];
    let i = 0;
    let key = 0;

    const pushText = (t) => {
        if (!t) return;
        out.push(<React.Fragment key={`t_${key++}`}>{t}</React.Fragment>);
    };

    while (i < text.length) {
        const caretIdx = text.indexOf('^', i);
        if (caretIdx === -1) {
            pushText(text.slice(i));
            break;
        }

        pushText(text.slice(i, caretIdx));

        const after = text[caretIdx + 1];
        if (after === '(') {
            const parsed = readBalancedParen(text, caretIdx + 1);
            if (parsed) {
                out.push(
                    <sup key={`s_${key++}`} className="align-super text-xs">
                        {parsed.content}
                    </sup>
                );
                i = parsed.endIdx + 1;
                continue;
            }
        }

        if (after) {
            const sup = after;
            out.push(
                <sup key={`s_${key++}`} className="align-super text-xs">
                    {sup}
                </sup>
            );
            i = caretIdx + 2;
            continue;
        }

        pushText('^');
        i = caretIdx + 1;
    }

    return <>{out}</>;
};
