import React from 'react';
import MathText from './MathText';
import { getKeypadForTopic } from './mathKeypadRegistry';

/**
 * MathKeypad — registry-driven symbol palette.
 *
 * Calls ``onInsert(text, caretOffset)`` so the parent input can splice the token
 * at the caret. Purely presentational; the parent owns the input + caret.
 */
const MathKeypad = ({ topic, onInsert, disabled = false }) => {
    const keys = getKeypadForTopic(topic);
    return (
        <div className="flex flex-wrap gap-2">
            {keys.map((k) => (
                <button
                    key={k.insert + k.label}
                    type="button"
                    disabled={disabled}
                    onClick={() => onInsert?.(k.insert, k.offset || 0)}
                    className="min-w-[2.75rem] h-10 px-3 rounded-lg border border-slate-200 bg-white hover:bg-indigo-50 hover:border-indigo-300 text-slate-700 shadow-sm transition-colors disabled:opacity-50 flex items-center justify-center"
                >
                    <MathText latex={k.label} />
                </button>
            ))}
        </div>
    );
};

export default MathKeypad;
