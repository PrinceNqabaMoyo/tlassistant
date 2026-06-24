import React from 'react';
import { CheckCircle2, XCircle, CircleHelp } from 'lucide-react';
import MathText from './MathText';
import { latexify } from './mathLatexify';

/**
 * WorkingPad — vertical, line-by-line working surface (mirrors how maths is
 * written on paper). Each line shows a live KaTeX preview of what the learner
 * typed. After diagnosis, per-line statuses pinpoint the first line that breaks.
 *
 * Controlled component:
 *   lines           array of strings
 *   onChange(lines) emits the updated lines
 *   statuses        optional array of {index, status} from the procedure tracker
 *   firstErrorStep  optional index of the first error line
 *   registerInput(fieldId, el)  lets the parent route keypad inserts to the
 *                   focused line
 *   onFocusField(fieldId)
 */
const statusIcon = {
    correct: <CheckCircle2 className="h-4 w-4 text-emerald-500" />,
    error: <XCircle className="h-4 w-4 text-rose-500" />,
    unparseable: <CircleHelp className="h-4 w-4 text-amber-500" />,
};

const WorkingPad = ({
    lines,
    onChange,
    statuses = null,
    firstErrorStep = null,
    registerInput,
    onFocusField,
}) => {
    const statusByIndex = React.useMemo(() => {
        const m = {};
        (statuses || []).forEach((s) => { m[s.index] = s.status; });
        return m;
    }, [statuses]);

    const updateLine = (idx, value) => {
        const next = [...lines];
        next[idx] = value;
        onChange(next);
    };

    const handleKeyDown = (idx, e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            const next = [...lines];
            next.splice(idx + 1, 0, '');
            onChange(next);
            setTimeout(() => onFocusField?.(`line-${idx + 1}`), 0);
        } else if (e.key === 'Backspace' && lines[idx] === '' && lines.length > 1) {
            e.preventDefault();
            const next = lines.filter((_, i) => i !== idx);
            onChange(next);
            setTimeout(() => onFocusField?.(`line-${Math.max(0, idx - 1)}`), 0);
        }
    };

    return (
        <div className="space-y-2">
            {lines.map((line, idx) => {
                const status = statusByIndex[idx];
                const isError = firstErrorStep === idx;
                return (
                    <div
                        key={idx}
                        className={`flex items-stretch gap-3 rounded-lg border px-3 py-2 ${
                            isError ? 'border-rose-300 bg-rose-50' : 'border-slate-200 bg-white'
                        }`}
                    >
                        <span className="w-6 shrink-0 text-xs text-slate-400 self-center text-right">{idx + 1}</span>
                        <input
                            ref={(el) => registerInput?.(`line-${idx}`, el)}
                            value={line}
                            onChange={(e) => updateLine(idx, e.target.value)}
                            onKeyDown={(e) => handleKeyDown(idx, e)}
                            onFocus={() => onFocusField?.(`line-${idx}`)}
                            placeholder={idx === 0 ? 'Type your first line of working…' : 'next line…'}
                            className="flex-1 min-w-0 font-mono text-sm bg-transparent outline-none text-slate-800"
                            spellCheck={false}
                        />
                        <div className="min-w-[5rem] flex items-center justify-end text-slate-700">
                            {line.trim() ? <MathText latex={latexify(line)} /> : null}
                        </div>
                        <span className="w-5 shrink-0 self-center">{status ? statusIcon[status] : null}</span>
                    </div>
                );
            })}
            <button
                type="button"
                onClick={() => onChange([...lines, ''])}
                className="text-xs font-medium text-indigo-600 hover:text-indigo-700"
            >
                + Add line
            </button>
        </div>
    );
};

export default WorkingPad;
